from discord.ext import commands
from os import getenv
import traceback
import re

bot = commands.Bot(command_prefix='!')

Italist = [("A", "𝓐"), ("B", "𝓑"), ("C", "𝓒"), ("D", "𝓓"), ("E", "𝓔"), ("F", "𝓕"), ("G", "𝓖"), ("H", "𝓗"), ("I", "𝓘"), ("J", "𝓙"), ("K", "𝓚"), ("L", "𝓛"), ("M", "𝓜"), ("N", "𝓝"), ("O", "𝓞"), ("P", "𝓟"), ("Q", "𝓠"), ("R", "𝓡"), ("S", "𝓢"), ("T", "𝓣"), ("U", "𝓤"), ("V", "𝓥"), ("W", "𝓦"), ("X", "𝓧"), ("Y", "𝓨"), ("Z", "𝓩"),
           ("a", "𝓪"), ("b", "𝓫"), ("c", "𝓬"), ("d", "𝓭"), ("e", "𝓮"), ("f", "𝓯"), ("g", "𝓰"), ("h", "𝓱"), ("i", "𝓲"), ("j", "𝓳"), ("k", "𝓴"), ("l", "𝓵"), ("m", "𝓶"), ("n", "𝓷"), ("o", "𝓸"), ("p", "𝓹"), ("q", "𝓺"), ("r", "𝓻"), ("s", "𝓼"), ("t", "𝓽"), ("u", "𝓾"), ("v", "𝓿"), ("w", "𝔀"), ("x", "𝔁"), ("y", "𝔂"), ("z", "𝔃")]


UnicodeEmoji = ["\N{Regional Indicator Symbol Letter N}",
                "\N{Regional Indicator Symbol Letter E}", "\N{Regional Indicator Symbol Letter W}", "\N{Gear}"]


def Itarep(line):
    Italine = line
    for before, after in Italist:
        Italine = newline.replace(before, after)
    return Italine


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_ready():
    print('Done Login')


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    if re.match(r'!', message.content):
        return
    sMNG = re.search(r'my new gear\i', message.content)
    if (sMNG is not None):
        for i in UnicodeEmoji:
            await message.add_reaction(i)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name="Italize")
async def Italize(ctx, arg):
    if ctx.author.bot:
        return
    re_arg = Itarep(arg)
    await ctx.send(re_arg)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
