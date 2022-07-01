import discord
import config
import time

bot = commands.Bot(command_prefix = config.invoke_char) #sets the invoke character. This is configured inside the config.py file. for example !help can be changed to  *help

@bot.event
async def on_ready(): #Ran when the bot is started
    print("Logged in as " + bot.user.name + "    (" + str(bot.user.id) + ")\n\n\n")
    if config.discord_activity == 1:
        await bot.change_presence(activity=discord.Game(name=config.discord_activity_name))
    elif config.discord_activity == 2:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config.discord_activity_name))
    elif config.discord_activity == 3:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.discord_activity_name))
    return

@bot.event
async def on_reaction_add(reaction, user):
    channelid = "920696623946940467"
    if reaction.message.channel.id != channelid:
        return
    if reaction.emoji == "👍":
        freegames = discord.utils.get(user.server.roles, name="Free games")
        await bot.add_roles(user, freegames

#uptime
@bot.command()
async def uptime(ctx):
    ptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
    uptime_var = discord.Embed(title=f"uptime",
                                description=str(uptime),
                                color=int(float(100)))
    await ctx.channel.send(embed=uptime_var)


bot.run(config.token)
