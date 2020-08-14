import discord
import logging

from client.logger import setup_logger
from client.setup import generate_channel_structure


class Client(discord.Client):
    def __init__(self, guild_id, /, run_setup, log_level,*,
                activity_name='Youtube',activity_type=discord.ActivityType.watching):
        """Initialize basic global variables and setting up logger for client"""
        super().__init__()
        self.GUILD = guild_id
        self.SETUP = run_setup
        self.ACTIVITY_NAME = activity_name
        self.ACTIVITY_TYPE = activity_type
        self.logger = setup_logger('', 'client.log', log_level=log_level)
        self.logger.info(f'Client class was initialized with {self.SETUP=} and {log_level=}')
    

    async def on_ready(self):
        """Setting up basic variables and create channels strucutre
        and create roles with basic privilages"""
        self.GUILD = self.get_guild(self.GUILD)
        self.logger.info(f'Client was connetcted with {self.GUILD} server')
        activity = discord.Activity(name=self.ACTIVITY_NAME,type=self.ACTIVITY_TYPE)
        await self.change_presence(activity=activity, status=discord.Status.online)

        # Setting up channels structure and generating roles
        if self.SETUP is True:
            for channel in self.get_all_channels():
                await channel.delete()
            self.logger.warning(f'All channels was deleted')
            await generate_channel_structure(self.GUILD)

        