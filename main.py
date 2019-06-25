import discord
client = discord.Client()
file = open('./token.txt', "r")
token = file.read()
file.close()


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("p!"):
        message.content = message.content[2:]
    print(message.content);





client.run(token)
