import os
import time
import discord
from discord.ext import commands


class GNBot(commands.Cog):
    """
    Bot object that handles actions on Discord. The primary function is to announce a players judgment in the voice
    channel.
    """
    token = os.environ.get('DISCORD_KEY')

    def __init__(self, bot: commands.Bot, messages: list):
        self.bot = bot
        self.message = messages

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Print the messages into the discord server.
        :return: Message in the Discord server.
        """
        for message in self.message:
            await self.send_message(message)

    @commands.command()
    async def gn(self, ctx, command: str):
        """
        Announce judgment to the voice channel.
        :param ctx: discord context parameter
        :return: JUDGMENT!
        """
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.play(discord.FFmpegPCMAudio(f"{command}.mp3"))
        except PermissionError:
            await ctx.send('Wait for the current playing music to end or use the stop command')
            return

        time.sleep(2)
        if voice.is_connected():
            await voice.disconnect()

    async def send_message(self, message):
        """
        Send a message into the desired channel ID.
        :param message: The message to send to the server.
        :return: None
        """
        channel = self.bot.get_channel(730551428963237985)
        await channel.send(f'{message}')
