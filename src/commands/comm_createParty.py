import asyncio
import discord

async def create_party_command(ctx: discord.Interaction):
    guild = ctx.guild
    nome_canal = f"{ctx.author.display_name}'s group"

    existing_channel = discord.utils.get(guild.voice_channels, name=nome_canal)
    if existing_channel:
        responseBot = await ctx.send(f"Já existe um canal de voz com o nome {nome_canal}. Entre nele")
        await asyncio.sleep(5)
        await responseBot.delete()
        return

    categoria_desejada = discord.utils.get(guild.categories, name="︶︶︶ Party Zone ︶︶︶")

    await guild.create_voice_channel(nome_canal, category=categoria_desejada)
    responseBot = await ctx.send(f"{nome_canal} criado com sucesso! Entrem para iniciarem sua jornada")

    await asyncio.sleep(9)

    await responseBot.delete()

    while True:
        canal_de_voz = discord.utils.get(guild.voice_channels, name=nome_canal)
        if len(canal_de_voz.voice_states) == 0:
            await canal_de_voz.delete()
            break
        await asyncio.sleep(2)
