<p align="center">
  <img src="https://balethon.ir/assets/img/logo.png" width="200" alt="Balethon">
</p>

## BalethonPlus

A library for creating bots in the [Bale](https://www.bale.ai) messenger

## Quick Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(message):
    await message.reply("Hello")


bot.run()
```

> You must replace `TOKEN` with the token which [BotFather](https://ble.ir/botfather) gives you in the [Bale](https://www.bale.ai) messenger

## Key Features

- **Easy**: Concise and high level programming interface
- **Fast**: Optimized and supports asynchronous programming
- **Documented**: Learn Balethon in depth with the documentation
- **Community**: Active and friendly community, you are sure to get answers to your questions
- **Design**: Support for functional as well as object-oriented designs
- **powerful**: Covers the [Bale](https://www.bale.ai) messenger's api and has useful tools to make your job easier
- **Flexible**: Unable to get deprecated and ready for unexpected responses from the [Bale](https://www.bale.ai) messenger's api
- **Intuitive**: Type-hinted and has great editor support
- **Extensible**: All balethon's systems are easily extensible

## Installing

```bash
pip install BalethonPlus
```

## Links

- [GitHub page](https://github.com/MohammaDeveloper/BalethonPlus)
- [Pypi page](https://pypi.org/project/BalethonPlus)
- [Bale news channel](https://ble.ir/balethon_plus)
- [Bale community chat group](https://ble.ir/balethon_plus_group)