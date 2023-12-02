import asyncio
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
    bot = commands.Bot(command_prefix='!', intents=intents)
            

    @bot.event
    async def on_ready():
        print('Bot iniciado!')
        # task_test.start()

    @bot.command()
    async def createParty(ctx, nome:str):
        guild = ctx.guild
        # nome_canal = f"{ctx.author.display_name}'s group"
        nome_canal = nome

        existing_channel = discord.utils.get(guild.voice_channels, name=nome_canal)
        if existing_channel:
            await ctx.send(f"Já existe um canal de voz com o nome {nome_canal}. Entre nele")
            return
        
        categoria_desejada = discord.utils.get(guild.categories, name="︶︶︶ Party Zone ︶︶︶")
        if not categoria_desejada:
            await ctx.send(f"A categoria 'NOME_DA_CATEGORIA' não foi encontrada. Certifique-se de que a categoria existe.")
            return
        
        await guild.create_voice_channel(nome_canal, category=categoria_desejada)
        await ctx.send(f"{nome_canal} criado com sucesso! Entrem pra iniciarem sua jornada")
        
        await asyncio.sleep(9)
        
        while True:
            canal_de_voz = discord.utils.get(guild.voice_channels, name=nome_canal)
            if len(canal_de_voz.voice_states) == 0:
                await canal_de_voz.delete()
                break
            await asyncio.sleep(2)

        


    @tasks.loop(seconds=3)
    async def task_test():
        channel = bot.get_channel(ID_CHANNEL_MSG)
        await channel.send('Bot inicializado')
    
    bot.run(BOT_TOKEN)


if __name__ == "__main__":   
    exec()