import discord
from discord.ext import commands, tasks

ID_CHANNEL_MSG = 1180187153452503110
BOT_TOKEN = "MTE4MDE5MzAxNTE1NTkyNTA2Mg.GBDhGD.SLnviOmRfV8sLwEN6flp6lfBUDPgL7TZIZgDUk" 


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