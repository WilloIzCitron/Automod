import discord
import datetime
import os
import webserver
from webserver import keep_alive
from datetime import datetime
TOKEN = os.environ.get("TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    myAct = discord.Activity(name='Tobot Galaxy | '+str(datetime.now())[:-15]+' | z!', type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.idle, activity=myAct,)
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    ToggleAntibadword.boolean = False
    ToggleAntiPing.boolean = False
    ToggleAntiLink.boolean = False

fp  = open('badwords.txt')
bad_list = [word.strip() for line in fp.readlines() for word in line.split(',') if word.strip()]

class ToggleAntibadword:
    def __init__(self, boolean):
        self.bool=boolean

class ToggleAntiPing:
    def __init__(self, boolean):
        self.bool=boolean

class ToggleAntiLink:
    def __init__(self, boolean):
        self.bool=boolean

@client.event
async def on_message(message):
    msg = message.content.lower()
    split = message.content.split()
    author = message.author.id
    messageAuthor = message.author

    print(f"Message Id {message.id}, message author {message.author}, content {message.content}, on {message.guild}")

    if message.content.startswith('z!toggle_antibadword_on'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntibadword.boolean = True
            await message.channel.send("toggle antibadword on")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!toggle_antibadword_off'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntibadword.boolean = False
            await message.channel.send("toggle antibadword off")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!toggle_antiping_on'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntiPing.boolean = True
            await message.channel.send("toggle antiping on")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!toggle_antiping_off'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntiPing.boolean = False
            await message.channel.send("toggle antiping off")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!toggle_antilink_on'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntiLink.boolean = True
            await message.channel.send("toggle antilink on")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!toggle_antilink_off'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            ToggleAntiLink.boolean = False
            await message.channel.send("toggle antilink off")
        else:
            await message.channel.send("You cant use this you needed Admin perm")

    if message.content.startswith('z!automod'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.administrator == True:
            if ToggleAntibadword.boolean == False or ToggleAntibadword.boolean == None:
                status = "<:matiaja:754703762865651774>"
            else:
                status = "<:ininyalaasw:754703762869846077>"
            if ToggleAntiPing.boolean == False  or ToggleAntiPing.boolean == None:
                statusAntiping = "<:matiaja:754703762865651774>"
            else:
                statusAntiping = "<:ininyalaasw:754703762869846077>"
            if ToggleAntiLink.boolean == False  or ToggleAntiLink.boolean == None:
                statusAntilink = "<:matiaja:754703762865651774>"
            else:
                statusAntilink = "<:ininyalaasw:754703762869846077>"
            embed = discord.Embed(title='Automod Status')
            embed.add_field(name='Anti Bad Word', value=str(status))
            embed.add_field(name='Anti Ping', value=str(statusAntiping))
            embed.add_field(name='Anti Link', value=str(statusAntilink))
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("You cant use this you needed Admin perm")
    
    if any(word in message.content for word in bad_list):
        if ToggleAntibadword.boolean == False:
            return
        else:
            await message.delete()
            await message.channel.send(f"<@{message.author.id}>, dont say this ok")

    if "@everyone" in message.content or "@here" in message.content:
        if ToggleAntiPing.boolean == False:
            return
        else:
            if author == message.guild.owner_id:
                return
            else:
                await message.channel.send(f"<@{message.author.id}>, dont ping others")

    if "https://" in message.content or "http://" in message.content:
        if ToggleAntiLink.boolean == False:
            return
        else:
            if author == message.guild.owner_id:
                return
            else:
                await message.delete()
                await message.channel.send(f"<@{message.author.id}>, dont send link here!")

    if message.content.startswith('z!generaterules'):
        if message.author.bot == True:
            return
        if message.author == client.user:
            return
        if message.author.guild_permissions.manage_guild == True:
            if 'rules' in message.channel.name:
                writerule = open("rules.txt")
                await message.channel.send(writerule.read())
            else:
                await message.channel.send('you arent on rule channel')
        else:
            await message.channel.send("You cant use this you need a Manage Server Permission?")

keep_alive()
client.run(TOKEN)

