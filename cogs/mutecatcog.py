#! ./.venv/bin/python
from discord.ext import commands
from logging import getLogger

class MuteCat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_voice = bot.get_channel(1028656118609743903)
        self.sleeplist = []

    def nowsleep(self, id):
        for user in self.sleeplist:
            if user.id == id:
                return False
        return True

    def sleeplistdel(self, id):
        tmp = []
        for user in self.sleeplist:
            print(f"{user.id} {id}")
            if user.id != id:
                tmp.append(user)
        self.sleeplist = tmp

    @commands.Cog.listener(name='on_voice_state_update')
    async def on_join(self, member, before, after):
        if before.channel != after.channel:
            # 入室
            if after.channel == self.channel_voice:
                for user in self.channel_voice.members:
                    await user.edit(mute=False)
                self.sleeplist = []

    @commands.group(name='neko')
    async def mutecat_cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("ぬるぽ")

    @mutecat_cog.command(name='sleep')
    async def voice_sleep(self, ctx):
        if self.nowsleep(ctx.author.id):
            self.sleeplist.append(ctx.author)
            await ctx.author.edit(mute=True)
            await ctx.reply("ねた　(¦3[___]")
        else:
            await ctx.reply("もうねてる　c(-ω-*c[＿＿]")

    @mutecat_cog.command(name='wakeup')
    async def voice_wakeup(self, ctx):
        if self.nowsleep(ctx.author.id) == False:
            self.sleeplistdel(ctx.author.id)
            await ctx.author.edit(mute=False)
            await ctx.reply("おきた　(:3[___]")
        else:
            await ctx.send("おきてる　c(･ω･*c[＿＿]")

    @mutecat_cog.command(name='list')
    async def voice_list(self, ctx):
        if len(self.sleeplist) > 0:
            message = "いま寝てる人たち zzz( ˘ω˘ )\n"
            for user in self.sleeplist:
                message += f"{user.name}\n"
            await ctx.reply(message)

def setup(bot):
    return bot.add_cog(MuteCat(bot))
