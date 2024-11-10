from discord.ext import commands
import asyncio
import discord
import random

players = []

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Let's you join the game!"""
        if len(players) >= 10:
            await ctx.send("You've reached the max team size!")
            return
        elif ctx.author.mention in players:
            await ctx.send(f"You're already in, {ctx.author.mention}!")
            return
        players.append(ctx.author.mention)
        await ctx.send(f"Thanks for joining, {ctx.author.mention}!")

    @commands.command()
    async def spin(self, ctx):
        """Spins the wheel!"""
        if len(players) < 1:
            await ctx.send("Sorry, nobody joined yet!")
        else:
            await ctx.send("Time to spin the wheel!")

            embed = discord.Embed(title = "Valorant", color = discord.Color.dark_magenta())
            embed.add_field(name = "Attackers", value = "\n")
            embed.add_field(name = "Defenders", value = "\n")
            message = await ctx.send(embed = embed)

            players_dupe = players.copy()
            attackers = []
            defenders = []

            for player in players:
                random_player = random.choice(players_dupe)
                players_dupe.remove(random_player)

                if len(attackers) < len(defenders):
                    attackers.append(random_player)
                else:
                    defenders.append(random_player)

                embed.set_field_at(0, name = "Attackers", value = "\n".join(attackers))
                embed.set_field_at(1, name = "Defenders", value = "\n".join(defenders))
                await asyncio.sleep(1)
                await message.edit(embed = embed)
            await ctx.send("Teams have been assigned!")

    @commands.command()
    async def reset(self, ctx):
        """Resets the player pool!"""
        players = []
        await ctx.send("The pool has been reset!")

def setup(bot):
    bot.add_cog(Core(bot))