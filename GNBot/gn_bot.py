import discord
from discord.ext import commands, tasks
import time


class GNBot(commands.Cog):
    """
    Bot object that handles actions on Discord. The primary function is to announce a players judgment in the voice
    channel.
    """
    token = 'Nzk3NTkzNjY3NDk2ODM3MTMx.X_ou_A.eqdwD2xrAAIm1PJNkEmxZfVFCsY'

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Print to the console to indicate the bot is now active.
        :return:
        """
        print('Bot online')

    @commands.command()
    async def hello(self, ctx,):
        """
        Announce judgment to the voice channel.
        :param ctx: discord context parameter
        :return: JUDGMENT!
        """
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.play(discord.FFmpegPCMAudio("dant.mp3"))
        except PermissionError:
            await ctx.send('Wait for the current playing music to end or use the stop command')
            return

        time.sleep(2)
        if voice.is_connected():
            await voice.disconnect()


bot = commands.Bot(command_prefix='!')
bot.add_cog(GNBot(bot))
bot.run(GNBot.token)
