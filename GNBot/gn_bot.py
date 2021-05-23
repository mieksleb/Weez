import discord
from discord.ext import commands, tasks
import time


class GNBot(commands.Cog):
    token = 'Nzk3NTkzNjY3NDk2ODM3MTMx.X_ou_A.eqdwD2xrAAIm1PJNkEmxZfVFCsY'

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot online')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.play(discord.FFmpegPCMAudio("dant.mp3"))
        except Exception:
            await ctx.send('Wait for the current playing music to end or use the stop command')
            return

        time.sleep(2)
        if voice.is_connected():
            await voice.disconnect()


bot = commands.Bot(command_prefix='!')
bot.add_cog(GNBot(bot))
bot.run(GNBot.token)
