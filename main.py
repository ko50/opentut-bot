import discord

from src import Bot

TOKEN = "MTMwNTA0Mzk1ODUwOTg2NzA2MA.GrAFDL.EdxaMtmFXAjIV9s7ggkQY-zArmVIRFkliZWP8Q"


intents = discord.Intents.default()
intents.message_content = True
client = Bot(intents=intents)
client.run(TOKEN)
