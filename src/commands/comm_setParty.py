import asyncio
import discord

from src.functions._createParty import _createParty

async def set_party_command(ctx: discord.Interaction):


    guild = ctx.guild
    nome_canal = f"{ctx.author.display_name}'s group"
    canal_de_voz = discord.utils.get(guild.voice_channels, name=nome_canal)

    if nome_canal not in [canal.name for canal in guild.voice_channels]:
        responsebot = await ctx.reply("Você não é lider party, não pode usar esse comando")
        await asyncio.sleep(12)        
        await responsebot.delete()
        return
    
    if len(canal_de_voz.members) >= 1:
        if ctx.author.display_name not in [member.display_name for member in canal_de_voz.members]:
            responsebot = await ctx.reply("O criador da party não está na party")
            await asyncio.sleep(12)
            await responsebot.delete()
            return
        else:
            await _createParty(canal_de_voz.members)

            responsebot = await ctx.reply("Party setada com sucesso")

            
            # Exemplo
            # [<Member id=410252296220311554 name='kaanun' global_name='Kaanun' bot=False nick=None guild=<Guild id=1180186430266413177 name='RPG Discord [Under develop]' shard_id=0 chunked=False member_count=4>>,
            # <Member id=565329611114676265 name='robbsuncc' global_name='Robbsun' bot=False nick=None guild=<Guild id=1180186430266413177 name='RPG Discord [Under develop]' shard_id=0 chunked=False member_count=4>>]


            await asyncio.sleep(12)
            await responsebot.delete()
            return
    else:
        responsebot = await ctx.reply("Não há ninguém na party")
        await asyncio.sleep(12)
        await responsebot.delete()
        return
        


