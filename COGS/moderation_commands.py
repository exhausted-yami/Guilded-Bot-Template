import guilded
from guilded.ext import commands
import asyncio
import glob
import os
import sys


class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="userinfo", description="Your command description", aliases=["who"])
    async def userinfo(self, ctx: commands.Context, *, user: str = None):
        if user is None:
            user = ctx.author
        else:
            user_mentions =  ctx.message.raw_user_mentions
            if len(user_mentions) > 0:
                user = await ctx.server.fetch_member(user_mentions[-1])
            else:
                try:
                    user = await ctx.server.fetch_member(user)
                except guilded.NotFound:
                    try:
                        user = await self.bot.fetch_user(user)
                    except guilded.NotFound:
                        user = None
        if user is None:
            await ctx.send(embed=guilded.Embed(
                title="Invalid User Selected",
                description="You selected an invalid user. Please try again!",
                color=guilded.Color.red()
            ))
        

        user_name = user.display_name
        user_id = user.id
        user_avatar = user.avatar
        user_bot = user.bot
        user_roles = user.roles

        embed = guilded.Embed(title=f"{user_name}'s Info", color=0xA7C6FF)
        embed.add_field(name="Username", value=user_name)
        embed.add_field(name="ID", value=user_id, inline=True)
        embed.add_field(name="Bot", value=user_bot, inline=True)
        embed.add_field(name="Role(s)", value=user_roles)
        embed.set_thumbnail(url=user_avatar)
        embed.set_footer(text="Test")

        # Send the embed
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(moderation(bot))
