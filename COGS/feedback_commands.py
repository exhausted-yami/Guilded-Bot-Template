import guilded
from guilded.ext import commands

class feedback(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot):
	bot.add_cog(feedback(bot))