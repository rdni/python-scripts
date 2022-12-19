import interactions
import math as m
from fractions import Fraction


bot = interactions.Client(token="YOUR_TOKEN_ID")

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
    if oddsof == "compressing boots":
        keysneeded = int(inputnumber) * 40
        sendMessage = f"To get {inputnumber}, you would on average need \
{keysneeded}."

    elif oddsof == "compressing boots complex":
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
    elif oddsof == "help":
        sendMessage = "In compressing boots complex it is keys, but in \
compressing boots it is the amount of compressing boots"
    else:
        sendMessage = f"Sorry {oddsof} is not a valid item added yet."

    await ctx.send(sendMessage)

@bot.command(
    name="killbot",
    description="This shuts down the bot.",
)
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
components=[killButtonConfirm, killButtonCancel])

@bot.component("killButtonConfirm")
async def killButtonConfirm(ctx: interactions.ComponentContext):
    print("Bot shutdown by command.")
    await ctx.send("Bot shutting down")
    exit()

@bot.component("killButtonCancel")
async def killButtonCancel(ctx: interactions.ComponentContext):
    await ctx.send("Bot not shutting down")

bot.start()