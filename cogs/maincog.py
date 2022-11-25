#! ./.venv/bin/python

# ---standard library---
import requests
import urllib

# ---third party library---
import discord
from discord.ext import commands

# ---local library---
import property

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def on_message(self, message):
        # Bot同士による会話を制限
        if message.author.bot:
            return
        # コマンドの場合処理をしない
        elif message.content[0] == '/':
            return

        if message.content.find('うんち') != 1:
            await message.channel.send('うんちぶりぶり')
            
        if message.content,find('うんこ') != 1:
            await message.channel.send('うんこぶりぶり')
        return

def setup(bot):
    return bot.add_cog(MainCog(bot))
