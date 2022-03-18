# dis-taipan  [![PyPI](https://img.shields.io/pypi/v/dis-taipan)](https://pypi.org/project/dis-taipan/)

50% [Dis-Snek](https://github.com/Discord-Snake-Pit/Dis-Snek) features that are either too undercooked for merging into the library proper
50%  "application specific" common code I want to use in most of my bots, but don't fit the philosophy of dis-snek itself.

A taipan is a dangerous australian snake.  I thought it was mildly amusing.

```
pip install dis-taipan
```

## Compatibility promises
Where possible, I avoid breaking changes.  While internals may change, the public interface will not.

Any features that are upstreamed and integrated into snek proper will be aliased, and still be accessible under the dis_taipan namespace.

I will bump the major version of taipan if I make breaking changes, or if I have to bump the *minimum* supported Snek version.

## Ready-to-Use Scales

### dis_taipan.sentry

Sets up a sentry.io hooks, intended to be as simple as possible.

To install, either set an environment variable called SENTRY_TOKEN (I recommend using [dotenv](https://pypi.org/project/python-dotenv/)), or put a string in the sentry_token attribute of your bot class.

Then call `bot.load_extension('dis_taipan.sentry')` to initialize the logger.

### dis_taipan.updater

Automatic updater.  Makes the following assumptions:
- You deploy using git, and the .git folder exists in production
- You have some kind of health check that will reboot the bot when it shuts down.

To install, call `bot.load_extension('dis_taipan.updater')`.  It'll do its magic every five minutes.
There is no configuration.

## Code Quality things:

### Protocols

[Protocols](https://peps.python.org/pep-0544/) are essentially the duck-typing equivelent of ABCs.  Think of them like Interfaces from C-like languages.

`SendableContext` is a protocol that mimics a Context with SendMixin.  Useful when typing error handlers.



