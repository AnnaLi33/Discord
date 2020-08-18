from discord.ext.commands import Bot
import random

BOT_Prefix = "!"


client = Bot(command_prefix= BOT_Prefix)

pasta_recipes = []

pastaFile = open("PastaRecipes", "r")
for i in pastaFile:
    pasta_recipes.append(i)
pastaFile.close()

@client.command()
async def test(ctx, arg):
    await ctx.channel.send(arg)

@client.command()
async def heyMeow(ctx):
    await ctx.channel.send('I heard you! {0.name}'.format(ctx.author))

@client.command()
async def Meowbaka(ctx):
    possible_responses = [
                 "Nani??",
                 "No You!",
                "... haha...",
                ":(",
                "That's what a baka would say >:)",
                "!!!!"
             ]
    await ctx.channel.send("{0} {1}".format(random.choice(possible_responses), ctx.author))

@client.command()
async def pasta(ctx):
    await ctx.channel.send("I recommend {0}".format(random.choice(pasta_recipes), ctx.author))

@client.command()
async def addpasta(ctx, message):
    string = message
    print( string[:4])
    if string[:5] == "https":
        for i in pasta_recipes:
            if i == message:
                await ctx.channel.send("HAH! I already knew that recipe.")
            else:
                print(message)
                savefile  = open("PastaRecipes", "w")
                pasta_recipes.append("\n{0}".format(message))
                for i in pasta_recipes:
                    savefile.write(i)
                await ctx.channel.send("Yum! Thank you for the {0}".format(message))

@client.command()
async def mostrecentpasta(ctx):
    await ctx.channel.send(pasta_recipes[-1])

@client.command()
async def myCookbook(ctx):
    Userpasta_recipes = []
    string = ctx.author
    string = str(string)+"recipes.txt"
    try:
        pastaFile = open(string, "r")
        for i in pastaFile:
            print(i)
            Userpasta_recipes.append(i)
        await ctx.channel.send("These are your recipes: {0}".format(Userpasta_recipes))
    except:
        pastaFile = open(string, "w")
        pastaFile.write("")
        await ctx.channel.send("Hello new chef, I've made a new cookbook for you.")

@client.command()
async def addrecipe(ctx, message):
    stringName = ctx.author
    stringName = str(stringName) + "recipes.txt" #unique pasta file
    string = message #link to the recipe
    print(string[:5]) #http
    Userpasta_recipes = [] #empty pasta recipe list
    try:
        pastaFile = open(stringName, "r")
        print("YEA")
        for i in pastaFile: #read all the lines in the file
            Userpasta_recipes.append(i) #add to list
            print("Sucessful read")
        print(Userpasta_recipes)
        if string[:5] == "https" and string[-1] == "/": #if the message is a website first 5 charas are https and last is /
            if len(Userpasta_recipes) == 0:
                Userpasta_recipes.append(message)
                savefile = open(stringName, "w")
                savefile.write(message)
                await ctx.channel.send("Exciting! This recipe has been added to {0}'s cookbook.".format(stringName))
            else:
                for i in Userpasta_recipes: # for each recipe in userpasta_recupes
                    if i == message: #if it exists
                        await ctx.channel.send("You've already added this recipe!")
                    else:
                        print(message)
                        savefile  = open(stringName, "w")
                        Userpasta_recipes.append("\n{0}".format(message))
                        for i in Userpasta_recipes:
                            savefile.write(i)
                        await ctx.channel.send("Exciting! This recipe has been added to {0}'s cookbook.".format(stringName))
                        return
    except:
        await ctx.channel.send("Looks like you have no Cookbook. Try the !myCookbook command to register your cookbook.")


# async def noU():
#     possible_responses = [
#         "Nani??"
#         "No You!"
#     ]
#     await client.say(random.choice(possible_responses))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()