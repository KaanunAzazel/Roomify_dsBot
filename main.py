import asyncio
import os
import dotenv
import discord
from discord.ext import commands, tasks

# IMPORT MODULES

from src.listeners.on_ready import on_ready_event
from src.commands.comm_createParty import create_party_command


dotenv.load_dotenv(dotenv.find_dotenv())

ID_CHANNEL_MSG = 1180187153452503110
BOT_TOKEN = os.getenv("BOT_TOKEN")


def exec():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        await on_ready_event(bot)

    @bot.hybrid_command(name="create-party", description="Create a party to join")
    async def createParty(ctx: discord.Interaction):
        await create_party_command(ctx)

    @tasks.loop(seconds=3)
    async def task_test():
        channel = bot.get_channel(ID_CHANNEL_MSG)
        await channel.send("Bot inicializado")

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    exec()
