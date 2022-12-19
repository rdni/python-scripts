import interactions
import math as m
import logging
from fractions import Fraction



bot = interactions.Client(token="YOUR_TOKEN_ID")

@bot.command(
    name="say",
    description="This will say what you entered.",
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def say(ctx: interactions.CommandContext, text: str):
    await ctx.send(text)

@bot.command(
    name="add",
    description="This will add what you entered.",
    options = [
        interactions.Option(
            name="num1",
            description="First number",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="num2",
            description="What you want to say",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def add(ctx: interactions.CommandContext, num1: int, num2: int):
    await ctx.send(f"{str(num1)} + {str(num2)} = {str(num1 + num2)}")
    
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
            name="numberofkeys",
            description="How many keys you opened",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def calculateodds(ctx: interactions.CommandContext, oddsof: str,\
 numberofkeys: int):
    logging.basicConfig(filename="logfile.txt", level=logging.INFO)
    logger1 = logging.getLogger("my-app")
    if oddsof == "compressing boots":
        percentChance = 2.5
        continueOn = True
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
        for i in range(int(numberofkeys)):
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
 give a prestige key."
        continueOn = False
    else:
        sendMessage = f"Sorry {oddsof} is not a valid item added yet."
        continueOn = False

#This code has been temporarily removed, might be put back later
    #if continueOn:
        #calculate = (amountofitem / numberofkeys) * 100
        #if calculate == percentChance:
            #sendMessage = f"You got exactly the hypothetical odds of \
#{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        #elif calculate < percentChance:
            #sendMessage = f"You got less than the hypothetical odds of \
#{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        #elif calculate > percentChance:
            #sendMessage = f"You got more than the hypothetical odds of \
#{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        #else:
            #sendMessage = f"Something broke lol"

    await ctx.send(sendMessage)

bot.start()