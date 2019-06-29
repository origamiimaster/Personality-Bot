print("[ INFO ]  Bot initializing.")
import markovify
print("[ INFO ]  Successfully imported markovify module.")
import os.path
print("[ INFO ] Successfully imported path")
import discord
print("[ INFO ]  Successfully imported discord module.")
client = discord.Client()
file = open('./token.txt', "r")
token = file.read()
print("[ INFO ]  Successfully processed discord bot token.")
file.close()
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f
commandList = []




@client.event
async def on_ready():
    print ("[ INFO ]  Bot connected to Discord.")
    print ("[ INFO ]  Bot ready; Listening for incoming messages.")    
    await client.change_presence (activity=discord.Game(name='with your words'))
    print("[ INFO ] GRABBING PERSONALITIES")
    personality_path = os.path.join(dir_path, os.listdir(dir_path)[2])
    personality_list = listdir_nohidden(personality_path)
    for p in personality_list:
        path = os.path.join(personality_path,p)
        file = open(path, "r")
        print(p[:-4])
        commandList.append(p[:-4])
        globals()[p[:-4]] = markovify.Text(file.read())
        #print(globals()[p[:4]].make_sentence())
        file.close()
    #print(jfk.make_sentence())
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
    if message.content[0] == "quote":
        string = message.content[1]+".make_sentence()"
        embed=discord.Embed(title="Quoting "+message.content[1], description=eval(string), color=0x00FF00)
        await message.channel.send(embed=embed)
        

    if message.content[0]=="help":
        embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xFFFF00)
        for command in commandList:
            embed.add_field(name=command, value="type p!quote "+command+" to mimic this person", inline= True)
        embed.add_field(name="mimic", value="Markov chains a sentence for a mentioned user, based off of past messages in the channel", inline= True)
        await message.channel.send(embed=embed)

        
    if message.content[0]=="yugioh":
        file = open('./'+message.content[1]+'.txt')
        text = file.read()
        file.close()
        text_model = markovify.Text(text)
        await message.channel.send(text_model.make_sentence())
client.run(token)




