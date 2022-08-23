"""
Automatically Checks for updates every 5 minutes and reboots the bot if there is a new version.

`bot.load_extension('dis_taipan.updater')`

"""
import asyncio
import subprocess

from naff import Client, Extension, listen, Task
from naff.models.naff.tasks import triggers

__all__ = ['Updater', 'setup']


class Updater(Extension):
    def __init__(self, bot: Client) -> None:
        self.bot = bot
        self.commit_id = (
            subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        )
        self.branch = (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .strip()
            .decode()
        )
        try:
            upstream = (
                subprocess.check_output(["git", "rev-parse", f"origin/{self.branch}"])
                .decode()
                .strip()
            )
            if upstream == self.commit_id:
                print(f"Currently running {self.commit_id} on {self.branch}")

        except subprocess.CalledProcessError as e:
            print(e)
            pass

    @listen()
    async def on_startup(self) -> None:
        try:
            self.update.start()
        except Exception as e:
            print(e)

    @Task.create(triggers.IntervalTrigger(minutes=5))
    async def update(self) -> None:
        loop = asyncio.get_running_loop()
        reboot = await loop.run_in_executor(None, self.check_for_update)

        if reboot:
            await self.bot.stop()

    def check_for_update(self) -> bool:
        try:
            subprocess.check_output(["git", "fetch"]).decode()
        except subprocess.CalledProcessError:
            return False
        commit_id = (
            subprocess.check_output(["git", "rev-parse", f"origin/{self.branch}"])
            .decode()
            .strip()
        )
        if commit_id != self.commit_id:
            print(f"origin/{self.branch} at {commit_id}")
            print("Update found, shutting down")
            subprocess.check_output(["git", "pull"]).decode()
            try:
                subprocess.check_output(["pipenv", "sync"]).decode()
            except Exception as c:
                print(c)
            return True
        return False


def setup(bot: Client) -> None:
    Updater(bot)
