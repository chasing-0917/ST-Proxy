import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# @bot.command()
# async def add(ctx, a: int, b: int):
#     await ctx.send(a + b)

# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a * b)
#
#
# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")
#
#
# @bot.command()
# async def cat(ctx):
#     await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def message(ctx):
    embed = discord.Embed(title="ST-Proxy", description="Welcome to ST-Proxy Group!", color=0x33FF33)

    embed.add_field(name="Name", value="ST团队，全称Share-Town，中文名鞋瞳，成立于2020年5月。", inline=False)
    embed.add_field(name="Attitude", value="我们拥有自己的DEV Team，规范的运营管理模式，和良好的服务态度。我们致力于向广大鞋圈和BOT圈用户提供最优质和最人性化的产品和服务。", inline=False)
    embed.add_field(name="Service", value="目前本团队所提供的产品有Gmail Proxy；并会在日后相继推出更多DC Proxy和球鞋监控组等诸多服务。", inline=False)
    embed.add_field(name="Purpose", value="我们所有的产品和服务都是为了让广大用户享受到更快捷，便利，和舒适的抢鞋体验。", inline=False)
    embed.add_field(name="Gratitude", value="期待与各位未来的合作。谢谢！", inline=False)

    await ctx.send(embed=embed)


bot.run('NzU1NjIyNjU5MTM5ODI5Nzcy.X2F-cA.NOXe8c6V4XhE_sCwdK1cjF5fGy8')
