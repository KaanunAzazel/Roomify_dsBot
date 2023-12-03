import asyncio
import discord

from typing import Literal
from src._class.player import Player


async def create_Character_command(ctx: discord.Interaction, nome: str, classe: str):
    # NOTe: Attr "Kwargs" trás no formato de dict
    # montar o player

    print(ctx)
    print('')
    newPlayer = Player(name=nome, dsID=ctx.author.name, character_class=classe)

    print(newPlayer)

    # capturar o canal do auhtor do comando

    pass
