from discord.ext import commands

class Automod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def on_message(self, message):
        msg = message.content.lower()
        split = message.content.split()
        author = message.author.id
        messageAuthor = message.author
        fp  = open('badwords.txt')
        bad_list = [word.strip() for line in fp.readlines() for word in line.split(',') if word.strip()]

        print(f"Message Id {message.id}, message author {message.author}, content {message.content}, on {message.guild}")
        
        if any(word in message.content for word in bad_list):
            await message.delete()
            await message.channel.send(f"<@{message.author.id}>, dont say this ok")

        if "@everyone" in message.content or "@here" in message.content:
            if author == message.guild.owner_id:
                return
            else:
                await message.channel.send(f"<@{message.author.id}>, dont ping others")

def setup(bot):
    bot.add_cog(Automod(bot))
