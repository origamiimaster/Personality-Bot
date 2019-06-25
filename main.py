import markovify
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
    if not message.content.startswith("p!"):
        return
    if message.author == client.user:
            return
    if message.author.bot: return
    message.content = message.content[2:]
    message.content = message.content.split(" ")
    if message.content[0]=="past":
        async for m in message.channel.history(limit=5):
            await message.channel.send(m.content)
    if message.content[0]=="mimic":
        text = ""
        async for m in message.channel.history(limit=None):
            if m.author.id == int(message.content[1]):
                if not m.content.startswith("p!"):
                    text = text +m.content+". "
        text_model = markovify.Text(text)
        

        #print(text)
        #await message.channel.send(text)
        await message.channel.send(text_model.make_sentence())




client.run(token)
