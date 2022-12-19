import interactions
import math as m
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
            name="amountofitem",
            description="How many you got",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="numberofkeys",
            description="How many keys you opened",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def calculateodds(ctx: interactions.CommandContext, oddsof: str,\
 amountofitem: int, numberofkeys: int):
    if oddsof == "compressing boots":
        percentChance = 2.5
        continueOn = True
    elif oddsof == "compressing boots complex":
        percentChance = 0.025
        emptyDrops = numberofkeys - amountofitem
        probability = m.pow(percentChance, float(amountofitem)) / m.pow(100 - percentChance, float(emptyDrops))
        sendMessage = f"Sorry {oddsof} is not implemented yet. This will in \
the future consider extra prestige keys and daily keys, that would lead to \
more potential compressing boots. Also for testing purposes that would be \
{Fraction(probability)}"
        continueOn = False
    else:
        sendMessage = f"Sorry {oddsof} is not a valid item added yet."
        continueOn = False
    if continueOn:
        calculate = (amountofitem / numberofkeys) * 100
        if calculate == percentChance:
            sendMessage = f"You got exactly the hypothetical odds of \
{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        elif calculate < percentChance:
            sendMessage = f"You got less than the hypothetical odds of \
{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        elif calculate > percentChance:
            sendMessage = f"You got more than the hypothetical odds of \
{percentChance} (you got {(amountofitem / numberofkeys) * 100})!"
        else:
            sendMessage = f"Something broke lol"
    await ctx.send(sendMessage)

bot.start()