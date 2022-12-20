import interactions
import math as m
import time
from fractions import Fraction
from discord.ext import commands


bot = interactions.Client(token="YOUR_TOKEN_ID")

@bot.command(
    name="help",
    description="Credits for the bot.",
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
    if page == 1:
        await ctx.send(f"Page {page} of help. In the command /calculateodds, \
there are currently 2 options for the command. You can do \"compressing \
boots\", and \"compressing boots complex\". Compressing boots takes the \
amount of compressing boots you want, and compressing boots complex takes the\
amount of keys you have. Next page is page {page + 1}, and is about areas")
    elif page == 2:
        await ctx.send(f"Page {page} of help. The current areas are: Spawn, \
Plains, Village, Outpost, Dark Forest, Aquarium, Desert, Mesa, Mineshaft, \
Deep Mine, Snow Zone, Absolute Zero, and the 2 zones with prestige \
requirements: Deep Sea (prestige 60) and Strange City (prestige 75). An area \
that is currently in development is the Nether. There is also an area \
accessible only by the command /lounge, which contains NPC versions of beta \
testers.")
    else:
        await ctx.send(f"Sorry, page {page} does not exist yet.")



@bot.command(
    name="credits",
    description="Credits for the bot.",
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
    await ctx.send(f"This bot was coded by redninja9854#2889 in Python, who \
was helped by Hollow#4029. You can access the source code of this bot at \
https://github.com/redninja9854/python-scripts/blob/main/discordBot.py")

@bot.command(
    name="calculatemulti",
    description="This will do calculations for multiplier in Newclicker.",
    options = [
        interactions.Option(
            name="tmulti",
            description="Temporary multiplier",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="pmulti",
            description="Permanent multiplier",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="rmulti",
            description="Rebirth multiplier",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def calculatemulti(ctx: interactions.CommandContext, tmulti: str,\
 pmulti: str, rmulti: str):
    calcuate = (float(tmulti) + float(pmulti)) * (float(rmulti) + 1)
    await ctx.send(f"The overall multiplier of a player with tmulti: {tmulti},\
 pmulti: {pmulti} and rmulti: {rmulti} is {calcuate}.")

@bot.command(
    name="calculateodds",
    description="This finds the odds of things.",
    options = [
        interactions.Option(
            name="oddsof",
            description="What thing you want the odds of",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="inputnumber",
            description="The amount of thing you want to calculate.",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def calculateodds(ctx: interactions.CommandContext, oddsof: str,\
 inputnumber: int):
    if oddsof.lower() == "compressing boots":
        keysneeded = int(inputnumber) * 40
        sendMessage = f"To get {inputnumber}, you would on average need \
{keysneeded}."
        ephemeral = False

    elif oddsof.lower() == "compressing boots complex":
        extrapkey = 0
        emptydrops = 0
        bootdrops = 0
        rkeydrops = 0
        rkeydropstotal = 0
        extrapkeytotal = 0
        bootdropstotal = 0
        pkeydropfromrkey = 0
        pkeydropfromrkeytotal = 0
        for i in range(int(inputnumber)):
            extrapkey += 0.06
            emptydrops += 0.75
            bootdrops += 0.025
            rkeydrops += 0.15
            if extrapkey >= 1:
                extrapkey -= 1
                extrapkeytotal += 1
                i = i - 2
            if bootdrops >= 1:
                bootdrops -= 1
                bootdropstotal += 1
            if rkeydrops >= 1:
                rkeydrops -= 1
                rkeydropstotal += 3
                pkeydropfromrkey += 0.15
                if pkeydropfromrkey >= 1:
                    pkeydropfromrkey -= 1
                    pkeydropfromrkeytotal += 1
                    i = i - 1

        sendMessage = f"On average you would get {bootdropstotal} compressing \
boots. This would come from {extrapkeytotal} extra prestige keys and \
{rkeydropstotal} drops from random key, of which {pkeydropfromrkeytotal} would\
 give a prestige key. There would be {emptydrops}.\nHidden values: \
bootdrops = {bootdrops}, extrapkey = {extrapkey}, rkeydrops = {rkeydrops} and \
pkeydropfromrkey = {pkeydropfromrkey}"
        ephemeral = False
    elif oddsof.lower() == "help":
        sendMessage = "In compressing boots complex it is keys, but in \
compressing boots it is the amount of compressing boots"
        ephemeral = False
    else:
        sendMessage = f"Sorry {oddsof} is not a valid item added yet."
        ephemeral = True

    await ctx.send(sendMessage, ephemeral=ephemeral)

@bot.command(
    name="clicksforitem",
    description="How many clicks are required for an item.",
    options = [
        interactions.Option(
            name="fortune",
            description="How much fortune you have",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="itemtype",
            description="The type of thing you want to calculate.",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="itemnumber",
            description="The amount of thing you want to calculate.",
            type=interactions.OptionType.INTEGER,
            required=False,
        ),
    ],
)
async def clicksforitem(ctx: interactions.CommandContext, fortune: int, itemtype: str, itemnumber = 1):
    continueOn = True
    if itemtype.lower() == "regular":
        itemsNeeded = 1
    elif itemtype.lower() == "compressed":
        itemsNeeded = 64
    elif itemtype.lower() == "super compressed":
        itemsNeeded = 4096
    elif itemtype.lower() == "ultra compressed":
        itemsNeeded = 262144
    elif itemtype.lower() == "mega compressed":
        itemsNeeded = 16777216
    else:
        await ctx.send(f"Sorry, {itemtype} is invalid.")
        continueOn = False
    if continueOn:
        clicksNeeded = float((itemsNeeded * itemnumber)) / float(fortune)
        if clicksNeeded < 1:
            clicksNeeded = 1
        await ctx.send(f"{itemnumber} {itemtype} items would take \
{m.ceil(clicksNeeded)} clicks with {fortune} fortune")



@bot.command(
    name="killbot",
    description="This shuts down the bot.",
)
@commands.has_permissions(administrator=True)
async def killbot(ctx: interactions.CommandContext):
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

@bot.component("killButtonConfirm")
async def killButtonConfirm(ctx: interactions.ComponentContext):
    print("Bot shutdown by command.")
    await ctx.send("Bot shutting down", ephemeral=True)
    exit()

@bot.component("killButtonCancel")
async def killButtonCancel(ctx: interactions.ComponentContext):
    await ctx.send("Bot not shutting down", ephemeral=True)

bot.start()