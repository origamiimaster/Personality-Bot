import discord
client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready")




client.run(token)
