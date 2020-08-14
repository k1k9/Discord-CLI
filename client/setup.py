import json
import discord
from client.logger import setup_logger

logger = setup_logger('setup', 'setup.log')
CONFIG_FILE = 'setup.json'


# Config file
with open(CONFIG_FILE, 'r', encoding='utf8') as f:
        CONFIG = json.load(f)


async def generate_channel_structure(guild):
    """ This function generate channels structure
    creating categories and channels under them
    @return a json data """
    for i in CONFIG['channels']:
        _name = CONFIG['channels'][i]['name']
        _icon = CONFIG['channels'][i]['icon']
        _text = CONFIG['channels'][i]['text']
        _voice = CONFIG['channels'][i]['voice']
        try:
            _category = await guild.create_category_channel(name=str(_name))
        except:
            for channel in _text:
                await guild.create_text_channel(f'{_icon}{channel}')
            continue

        for channel in _text:
            await _category.create_text_channel(f'{_icon}{channel}')

        for channel in _voice:
            await _category.create_voice_channel(f'{_icon} {channel}')
        
        logger.info(f'Created new category {_name=} with {len(_text)} '\
                        f'text channels and {len(_voice)} voice')
    logger.info('Channel structure was generated')


async def generate_roles(guild):
    """ This function create roles with privilages """
    # Administrator
    await guild.create_role(name="Administrator",
                        colour=discord.Colour.from_rgb(169,64,42),
                        mentionable=True,
                        permissions=discord.Permissions.all(),
                        reason="Created by bot in setup")

    # Moderator
    _perms_moderator = discord.Permissions(kick_members=True,
            ban_members=True,
            priority_speaker=True,
            manage_messages=True,
            attach_files=True,
            mention_everyone=True,
            mute_members=True,
            deafen_members=True,
            move_members=True,
            manage_nicknames=True)
    await guild.create_role(name="Moderator",
                            colour=discord.Colour.from_rgb(54,198,193),
                            mentionable=True,
                            permissions=_perms_moderator,
                            reason="Created by bot in setup")
    
    # Patron
    await guild.create_role(name="Patron",
                            colour=discord.Colour.from_rgb(255,206,51),
                            mentionable=True,
                            permissions=discord.Permissions.general(),
                            reason="Created by bot in setup")

    # Patron
    await guild.create_role(name="Bot",
                            colour=discord.Colour.from_rgb(231,255,250),
                            mentionable=False,
                            permissions=discord.Permissions.general(),
                            reason="Created by bot in setup")

    # Other roles with default privilages
    for role in CONFIG['roles']:
        await guild.create_role(name=role,
                            mentionable=False,
                            permissions=discord.Permissions.general(),
                            reason="Created by bot in setup")

    logger.info('Roles was created')