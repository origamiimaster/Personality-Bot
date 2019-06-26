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
        s = message.content[1]
        message.content[1] = ''.join(filter(lambda x: x.isdigit(), s))
        text = ""
        counter=0
        async for m in message.channel.history(limit=2500):
            if counter < 500:

                if m.author.id == int(message.content[1]):
                    if not m.content.startswith("p!"):
                        if not m.content == "":
                            if m.content[-1:]=="?" or m.content[-1:]=="!"or m.content[-1:]==".":
                                text = text +m.content+" "
                                counter =counter +1
                            else:
                                text = text +m.content+". "
                                counter =counter +1
        print(text)
        text_model = markovify.Text(text)
        sentence = ""
        counter = 0
        while sentence=="" or sentence ==None:
            counter =counter +1
            sentence = text_model.make_sentence()
            print(sentence)
            if sentence != "" and sentence !=None:
                break
            if counter > 500:
                sentence = "FAILED"
                break
        #print(text)
        #await message.channel.send(text)
        await message.channel.send(sentence)
    if message.content[0]=="jfk":
        file = open('./jfk.txt')
        text = file.read()
        file.close()
        text_model = markovify.Text(text)

        await message.channel.send(text_model.make_sentence())
    if message.content[0]=="help":
        embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xFFFF00)

        embed.add_field(name="mimic", value="markov chains a sentence for a mentioned user, based off of past messages in the channel", inline= True)
        embed.add_field(name="jfk", value="markov chains a sentence from President John Fitzgerald Kennedy's speeches", inline= True)


        await message.channel.send(embed=embed)            

    
        #message.channel.send({embed: {
          #color: 3447003,
          #description: "A very simple Embed!"
        #}});
client.run(token)
