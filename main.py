import discord
from discord.ext import commands
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.event
async def on_member_join(member):
    server_id = 1141826875753250959
    welcome_channel_id = 1142570977562218547
    welcome_message = {
        "title": "Welcome to **Moniker!**",
        "description": f"Hello {member.mention}, welcome to our Discord server! We're thrilled to have you join our community.\n\nHere, you'll find a diverse and engaging group of individuals who share your interests. Whether you're here to connect, learn, or simply have fun, you're in the right place.\n\nPlease take a moment to read through our welcome message in the <#{welcome_channel_id}> channel. It contains important information that will ensure everyone has a positive and respectful experience.",
        "color": 2632496,
        "author": {
            "name": "Moniker",
            "url": "https://mnkr.cc",
            "icon_url": "https://media.discordapp.net/attachments/1141826944875384923/1142570566549786734/logo-discord-bot-webhook.png",
        },
        "footer": {
            "text": "Endless Sharing within a single platform.",
            "icon_url": "https://media.discordapp.net/attachments/1141826944875384923/1142570566549786734/logo-discord-bot-webhook.png",
        },
        "thumbnail": {
            "url": "https://media.discordapp.net/attachments/1141826944875384923/1142570566549786734/logo-discord-bot-webhook.png?width=700&height=700"
        },
    }

    role_id = 1142590045753184277

    guild = bot.get_guild(server_id)
    welcome_channel = guild.get_channel(welcome_channel_id)
    role = guild.get_role(role_id)

    await member.send(embed=discord.Embed.from_dict(welcome_message))
    await member.add_roles(role)


# Replace 'YOUR_TOKEN' with your actual bot token
bot.run(config["TOKEN"])
