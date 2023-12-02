import discord

async def on_ready_event(bot):
    print("Bot iniciado!")
    await bot.tree.sync()
    # task_test.start()
