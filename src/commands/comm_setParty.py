import asyncio
import discord

async def set_party_command(ctx: discord.Interaction):


    guild = ctx.guild
    nome_canal = f"{ctx.author.display_name}'s group"
    canal_de_voz = discord.utils.get(guild.voice_channels, name=nome_canal)

    if nome_canal not in [canal.name for canal in guild.voice_channels]:
        responsebot = await ctx.reply("Você não é lider party, não pode usar esse comando")
        await asyncio.sleep(12)        
        await responsebot.delete()
        return

    if ctx.author.display_name not in [member.display_name for member in canal_de_voz.members]:
        responsebot = await ctx.reply("O criador da party não está na party")
        await asyncio.sleep(12)
        await responsebot.delete()
        return
    else:
        responsebot = await ctx.reply("Party setada com sucesso")
        await asyncio.sleep(12)
        await responsebot.delete()
        return
        


