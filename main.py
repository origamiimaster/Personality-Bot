print("[ INFO ]  Bot initializing.")
import markovify
print("[ INFO ]  Successfully imported markovify module.")
import os.path
print("[ INFO ]  Successfully imported path")
import discord
print("[ INFO ]  Successfully imported discord module.")
client = discord.Client()
file = open('./token.txt', "r")
token = file.read()
print("[ INFO ]  Successfully processed discord bot token.")
file.close()
dir_path = os.path.dirname(os.path.realpath(__file__))

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
    print("[ INFO ]  GRABBING PERSONALITIES")
    personality_path = os.path.join(dir_path, os.listdir(dir_path)[2])[:-len('token.txt/')]
    personality_list = listdir_nohidden("personality")
    for p in personality_list:
        # print(p)
        path = os.path.join(personality_path + "/personality", p)
        # print(path)
        file = open(path, "r")
        print("[ INFO ]  Loading: " +p[:-4])
        commandList.append(p[:-4])
        globals()[p[:-4]] = markovify.Text(file.read())
        file.close()
    print("[ INFO ]  Completed loading personality folder")
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
        print("Mimicing: ")
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
        text_model = markovify.Text(text)
        sentence = ""
        counter = 0
        while sentence=="" or sentence ==None:
            counter =counter +1
            sentence = text_model.make_sentence(tries=5000)
            if not sentence != "" and sentence !=None:            
                sentence = "ERROR: Sentence generation failure."
                print ("[ FAIL ]  Sentence generation failure.")
                break
        await message.channel.send(sentence)
        print ("[ INFO ]  Mimic sentence generation for target user "+message.content[1]+" successful.")
    if message.content[0] == "quote":
        if len(message.content) <= 1:
            string = "Try adding one of these options: "
            for c in commandList:
                string += c +", "
            await message.channel.send(string+"or try the mimic command")
        else:
            if not message.content[1] in globals():
                await message.channel.send("That is not a valid option for this command")
            else:
                # string = message.content[1]+".make_sentence(tries=5000)"
                # text = eval(string)
                # if text =="" or text == None:
                #         embed=discord.Embed(title="Quoting "+message.content[1], description="There was an error generating a sentence, please try again or with another user", color=0xFF0000)
                # embed=discord.Embed(title="Quoting "+message.content[1], description=eval(string), color=0x00FF00)
                # await message.channel.send(embed=embed)
                pass
        if len(message.content) > 2:
            await message.channel.send("Just a reminder, this command currently only works with one input.")
    if message.content[0]=="help":
        embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xFFFF00)
        for command in commandList:
            embed.add_field(name=command, value="type p!quote "+command+" to mimic this person", inline= True)
        embed.add_field(name="mimic", value="Markov chains a sentence for a mentioned user, based off of past messages in the channel", inline= True)
        await message.channel.send(embed=embed)
    if message.content[0]=="info":
        embed=discord.Embed(title="Personality-Bot", description="Mimicking personas with Markov Chains", color=0x010101)
        embed.add_field(name="created by", value="Origamiimaster#2189 and WellDone#7408", inline=True)
        embed.add_field(name="where to start", value="try asking the bot to mimic another user with p!mimic @user#0001", inline = True)
        embed.add_field(name="common issue #1", value="mimic doesn't work? probably because the user does not have enough messages in this channel. try with more messages or in a different channel", inline = True)
        embed.add_field(name="common issue #2", value="why doesn't quote work on the new text file i loaded? try making sure that the text is long enough, or try restarting the bot. also check your text for any offending non unicode characters", inline = True)
        await message.channel.send(embed=embed)
client.run(token)


