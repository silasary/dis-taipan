import naff


def test_load() -> None:
    bot = naff.Client()
    bot.load_extension("dis_taipan.botguild")
    bot.load_extension("dis_taipan.sentry")
    bot.load_extension("dis_taipan.updater")
    print(repr(bot.ext))
    assert len(bot.ext) == 2
