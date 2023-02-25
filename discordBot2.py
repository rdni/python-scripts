import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)
client.run("MTA1Mzc2Njc2NjUxNTQ1Mzk5NA.Gkf_UG.Qbj-kutS7gbavnSQ9gg-qJ9RTmzbXeOTUoY_Ns")

@client.command()
async def say(ctx, *, message):
    await ctx.send(message)
