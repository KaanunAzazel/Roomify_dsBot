import os
import dotenv
import discord
from discord.ext import commands, tasks

dotenv.load_dotenv(dotenv.find_dotenv())

ID_CHANNEL_MSG = 1180187153452503110
BOT_TOKEN = os.getenv("BOT_TOKEN")


def exec():
    intents = discord.Intents.default()
    intents.message_content = True 
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print('Bot iniciado!')
        task_test.start()

    @tasks.loop(seconds=3)
    async def task_test():
        channel = bot.get_channel(ID_CHANNEL_MSG)
        await channel.send('Bot inicializado')
    
    bot.run(BOT_TOKEN   )


if __name__ == "__main__":   
    exec()