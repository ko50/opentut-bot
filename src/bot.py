import discord
from discord import TextChannel
from discord.ext import tasks

class Bot(discord.Client):
    def init(self, intents: discord.Intents):
        intents = discord.Intents.default()
        intents.message_content = True

        # super().__init__(intents=intents)

    # 起動時
    async def on_ready(self):
        print("Ready!")

    # メッセージ受信時
    async def on_message(self, message: discord.Message):
        # 自身が送信したメッセージには反応しない
        if message.author == self.user:
            return

        # Botのメッセージには反応しない
        if message.author.bot:
            return

        # ユーザーからメンションされていない場合は何もしない
        if not self.user in message.mentions:
            return

        if "参加" in message.content:
            answer = "参加登録しました！"

            await self.send_message(answer, message.channel)

    async def send_message(self, message: str, channel: TextChannel):
        print(message)
        await channel.send(message)

    @tasks.loop(weeks=1)
    async def sendWeekly(self):
        ...

    # async def start(self, token: str):
    #     await self.run(token)
