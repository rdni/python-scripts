import interactions
import math as m
import time
from fractions import Fraction
from discord.ext import commands



bot = interactions.Client(token="YOUR_TOKEN_ID")

@bot.command(
    name="version",
    description="Credits for the bot.",
)
async def version(ctx: interactions.CommandContext):
    version = await getVersion()
    await ctx.send(f"The current version of the bot is {version}.")

async def getVersion():
    return "public-0.1.4"

@bot.command(
    name="help",
    description="Help for the bot.",
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
        await ctx.send(f"Page {page} of help. There are 7 commands: /version, \
/credits, /help, /calculatemulti, /calculateodds, /clicksforitem and /fortune.\
 In the command /calculateodds, there are currently 3 options for the command.\
 You can do \"compressing boots\", \"compressing boots complex\" and \
\"fortune\". Compressing boots takes the amount of compressing boots you want,\
 compressing boots complex takes theamount of keys you have, and fortune takes\
 the amount of keys you have. Next page is page {page + 1}, and is about \
areas.")
    elif page == 2:
        await ctx.send(f"Page {page} of help. The current areas are: Spawn, \
Plains, Village, Outpost, Dark Forest, Aquarium, Desert, Mesa, Mineshaft, \
Deep Mine, Snow Zone, Absolute Zero, and the 3 zones with prestige \
requirements: Arena (prestige 30), Deep Sea (prestige 60) and Strange City \
(prestige 75). An area that is currently in development is the Nether. There \
is also an area accessible only by the command /lounge, which contains NPC \
versions of beta testers. Next page is page {page + 1}, and is about gear.")
    elif page == 3:
        await ctx.send(f"Page {page} of help. The current most expensive gear \
in the game is ice knight, however the leggings and boots are not regarded as \
the best. Snowy boots and Supreme IVs are considered better boots, with Snowy \
boots giving speed 5 and +25% money, and Supreme IVs giving speed 6. There is \
some disagreement about which is better. Zombie leggings give +75% money, \
however give slowness 3, so at rebirth 7, with autoprestige and deep sea \
key, it is recommended to use zombie leggings. Next page is page {page + 1}, \
and is about rebirths")
    elif page == 4:
        await ctx.send(f"Page {page} of help. Rebirth tokens and 0.5x rebirth \
multiplier are given, as a reward on rebirth. Rebirth multiplier is \
considered good because it is multiplicative (see /calculatemulti to work out \
your own multiplier), while rebirth tokens are considered good because they \
can give unique items. It is best to first get autoprestige, to help get you \
to prestige 60 (Deep sea is unlocked) faster. Then get the deep sea key, so \
travel time is removed, and zombie leggings can be used more efficiently. \
After that, if you want, you can get the soul talisman, but other than that, \
just get bonus prestige vouchers. Next page is page {page + 1}, and is about \
bugs.")
    elif page == 5:
        await ctx.send(f"Page {page} of help. So far there have been very \
small amount of game breaking bugs, but there is currently one unresolved one,\
 that no-one seems to know how to fix: wiping of certain people's stats. This \
has only been found to effect the players noahforse21, T_Crazy and txged. If \
anybody knows a fix for data loss, similar to this, please contact Akenolein. \
This bug causes variables from variables.cvs in Skript to disappear. An \
attempted fix was implemtented, but it is still unknown if it worked.")
    else:
        await ctx.send(f"Sorry, page {page} does not exist yet.")

async def sendMessage(ctx: interactions.CommandContext, message: str, ephemeral: bool, embeds = None):
    await ctx.send(message, embeds=embeds, ephemeral=ephemeral)




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
 give a prestige key. There would be {emptydrops} empty drops."
        ephemeral = False
    elif oddsof.lower() == "fortune":
        ftoken = 0
        mtoken = 0
        ftokentotal = 0
        mtokentotal = 0
        for i in range(int(inputnumber)):
            mtoken += 0.075
            ftoken += 0.15
            if mtoken >= 1:
                mtoken -= 1
                mtokentotal += 1
            if ftoken >= 1:
                ftoken -= 1
                ftokentotal += 3
        totalfortune = int(ftokentotal) * 2 + int(mtokentotal) * 7
        sendMessage = f"{inputnumber} keys would give you around {totalfortune} \
fortune"
        ephemeral = False
    elif oddsof.lower() == "help":
        sendMessage = "In compressing boots complex you input amount of keys, \
in compressing boots you input the amount of compressing boots and in \
fortune you input amount of keys."
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
    name="fortune",
    description="Fortune given on average.",
    options = [
        interactions.Option(
            name="fortunetokens",
            description="How much fortune you have",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="megatokens",
            description="The type of thing you want to calculate.",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def fortune(ctx: interactions.CommandContext, fortunetokens: int, megatokens: int):
    totalfortune = int(fortunetokens) * 2 + int(megatokens) * 7
    await ctx.send(f"You would get {totalfortune} fortune, on average, from \
{fortunetokens} fortune tokens and {megatokens} mega fortune tokens.")

@bot.command(
    name="changelogadd",
    description="This shuts down the bot.",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
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
            await sendto.send(f"Changelog entry (version '{version}' discord bot): {changelogtext}")
            await ctx.send("Command executed", ephemeral=True)
        else:
            sendto = await ctx.get_channel()
            await sendto.send(f"Changelog entry: {changelogtext}")
            await ctx.send("Command executed", ephemeral=True)
    else:
            await ctx.send("Incorrect password", ephemeral=True)



@bot.command(
    name="killbot",
    description="This shuts down the bot.",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
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