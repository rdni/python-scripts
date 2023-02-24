import interactions
import math as m
import time
from fractions import Fraction
from discord.ext import commands
from interactions.utils.get import get



bot = interactions.Client(token="tokenId")

@bot.command(
    name="version",
    description="Version of the bot.",
    dm_permission=True,
)
async def version(ctx: interactions.CommandContext):
    version = await getVersion()
    await ctx.send(f"The current version of the bot is {version}.")

async def getVersion():
    return "alpha-1"

async def getPage(page: int):
    if page == 1:
        return [f"Page {page} of help. This bot is a testing bot, which is \
still in beta, and is for the Mubble devs group", False]
    else:
        return [f"Sorry, page {page} does not exist yet.", False]

@bot.command(
    name="help",
    description="Help for the bot.",
    dm_permission=True,
    options = [
        interactions.Option(
            name="page",
            description="Page of help you want to access",
            type=interactions.OptionType.INTEGER,
            required=False,
        ),
    ]
)
async def help(ctx: interactions.CommandContext, page = 1):
    sendMessage = await getPage(page)
    await ctx.send(sendMessage[0], ephemeral=sendMessage[1])

async def sendMessage(ctx: interactions.CommandContext, message: str, ephemeral: bool, embeds = None):
    await ctx.send(message, embeds=embeds, ephemeral=ephemeral)




@bot.command(
    name="credits",
    description="Credits for the bot.",
    dm_permission=True,
)
async def credits(ctx: interactions.CommandContext):
    creditsButton = interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Credits!",
        custom_id="creditsPressed",
    )
    await ctx.send(components=creditsButton)

@bot.component("creditsPressed")
async def creditsPressed(ctx: interactions.ComponentContext):
    await ctx.send(f"This bot was coded by redninja9854#2889 in Python. You \
can access the source code of this bot at \
https://github.com/redninja9854/python-scripts/blob/main/discordBot.py")


@bot.command(
    name="changelogadd",
    description="This adds a changelog message.",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
    dm_permission=False,
    options = [
        interactions.Option(
            name="password",
            description="Double checking its you",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="changelogtext",
            description="What should be entered to the changelog",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="discord",
            description="True for if it is a bot changelog.",
            type=interactions.OptionType.BOOLEAN,
            required=False,
        ),
    ]
)
async def changelogadd(ctx: interactions.CommandContext, password: str, changelogtext: str, discord=False):
    correctPassword = "P4SSW0RD"
    if correctPassword == password:
        if discord:
            sendto = await ctx.get_channel()
            version = await getVersion()
            await ctx.send("Command executed", ephemeral=True)
            await sendto.send(f"Changelog entry (version '{version}' discord bot): {changelogtext}")
        else:
            sendto = await ctx.get_channel()
            await ctx.send("Command executed", ephemeral=True)
            await sendto.send(f"Changelog entry: {changelogtext}")
    else:
            await ctx.send("Incorrect password", ephemeral=True)

@bot.command(
    name="changelogedit",
    description="This edits a changelog message.",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
    dm_permission=False,
    options = [
        interactions.Option(
            name="channelid",
            description="Channel the message is in",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="messageid",
            description="Message to edit",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="changelogtext",
            description="What should be entered to the changelog",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="discord",
            description="True for if it is a bot changelog.",
            type=interactions.OptionType.BOOLEAN,
            required=False,
        ),
    ]
)
async def changelogedit(ctx: interactions.CommandContext, channelid: str, messageid: str, changelogtext: str, discord=False):
    if discord:
        version = await getVersion()
        message = await get(bot, interactions.message, object_id=messageid)
        await ctx.send("Command executed", ephemeral=True)
        await message.edit(channelid, messageid, f"Changelog entry (version '{version}' discord bot): {changelogtext}")
    else:
        sendto = await ctx.get_channel()
        await ctx.send("Command executed", ephemeral=True)
        await sendto.send(f"Changelog entry: {changelogtext}")

@bot.command(
    name="killbot",
    description="This shuts down the bot.",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
    dm_permission=False,
    options = [
        interactions.Option(
            name="password",
            description="Double checking its you",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def killbot(ctx: interactions.CommandContext, password: str):
    correctPassword = "P4SSW0RD"
    if correctPassword == password:
        killButtonConfirm = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="Confirm",
            custom_id="killButtonConfirm",
        )
        killButtonCancel = interactions.Button(
            style=interactions.ButtonStyle.DANGER,
            label="Cancel",
            custom_id="killButtonCancel",
        )
        await ctx.send("Are you sure you want to end the program?", \
components=[killButtonConfirm, killButtonCancel], ephemeral=True)
    else:
        await ctx.send("Incorrect password", ephemeral=True)

@bot.component("killButtonConfirm")
async def killButtonConfirm(ctx: interactions.ComponentContext):
    print("Bot shutdown by command.")
    await ctx.send("Bot shutting down", ephemeral=True)
    exit()

@bot.component("killButtonCancel")
async def killButtonCancel(ctx: interactions.ComponentContext):
    await ctx.send("Bot not shutting down", ephemeral=True)

bot.start()