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

## Installing

```bash
pip install BalethonPlus
```

## Links

- [GitHub page](https://github.com/MohammaDeveloper/BalethonPlus)
- [Pypi page](https://pypi.org/project/BalethonPlus)
- [Bale news channel](https://ble.ir/balethon_plus)
- [Bale community chat group](https://ble.ir/balethon_plus_group)