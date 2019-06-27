print("[ INFO ]  Bot initializing.")
import markovify
print("[ INFO ]  Successfully imported markovify module.")
import discord
print("[ INFO ]  Successfully imported discord module.")
client = discord.Client()
file = open('./token.txt', "r")
token = file.read()
print("[ INFO ]  Successfully processed discord bot token.")
file.close()

@client.event
async def on_ready():
    print("[ INFO ]  Bot ready; Listening for incoming messages.")

@client.event
async def on_message(message):
    if not message.content.startswith("p!"):
        return
    if message.author == client.user:
        return
    if message.author.bot: return
    message.content = message.content[2:]
    message.content = message.content.split(" ")
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
        #print(text)
        text_model = markovify.Text(text)
        sentence = ""
        counter = 0
        while sentence=="" or sentence ==None:
            counter =counter +1
            sentence = text_model.make_sentence()
            #print(sentence)
            if sentence != "" and sentence !=None:
                break
            if counter > 500:
                sentence = "ERROR: Sentence generation failure."
                print ("[ FAIL ]  Sentence generation failure.")
                break
        #print(text)
        #await message.channel.send(text)
        await message.channel.send(sentence)
        print ("[ INFO ]  Mimic sentence generation for target user "+message.content[1]+" successful.")
    if message.content[0]=="jfk":
        file = open('./jfk.txt')
        text = file.read()
        file.close()
        text_model = markovify.Text(text)

        await message.channel.send(text_model.make_sentence())
        print ("[ INFO ]  JFK sentence generation successful.")

    if message.content[0]=="trumpTweets":
        file = open('./trumpTweets.txt')
        text = file.read()
        file.close()
        text_model = markovify.Text(text)

        await message.channel.send(text_model.make_sentence())
        print ("[ INFO ]  TrumpTweets sentence generation successful.")

    if message.content[0]=="obama":
        file = open('./obama.txt')
        text = file.read()
        file.close()
        text_model = markovify.Text(text)

        await message.channel.send(text_model.make_sentence())
        print ("[ INFO ]  Obama sentence generation successful.")

    if message.content[0]=="help":
        embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xFFFF00)

        embed.add_field(name="mimic", value="Markov chains a sentence for a mentioned user, based off of past messages in the channel", inline= True)
        embed.add_field(name="jfk", value="Markov chains a sentence from President John Fitzgerald Kennedy's speeches", inline= True)
        embed.add_field(name="trumpTweets", value="Markov chains a sentence from President Donald John Trump's Tweets", inline= True)
        embed.add_field(name="obama", value="Markov chains a sentence from President Barrack Hussein Obama's Tweets", inline= True)

        await message.channel.send(embed=embed)
    
        #message.channel.send({embed: {
          #color: 3447003,
          #description: "A very simple Embed!"
        #}});
client.run(token)
