import discord
import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all(), help_command=None)

welcome_channel = 123456789

#----------------------------------------------------------------------------------------------------------------------> Ready
@bot.event
async def on_ready():
    print(f"| Logged in as - {bot.user.name}")
    print(f"| Bot ID - {bot.user.id}")
    print(f"| Discord Version - {discord.__version__}")

    print(f"\n {bot.user} using: ✅")

print("\nMessage Author using: ✅")

#----------------------------------------------------------------------------------------------------------------------> Join
print(f"Join system using: ✅")
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    embed = discord.Embed(description=f"Welcome {member.mention}", 
                          color=discord.Color.from_rgb(17, 31, 47),
                        )
    
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="", value=f"I'm glad you're here! Read the rules.", inline=False)



    
    role = discord.utils.get(member.guild.roles, name="Tag")
    await member.add_roles(role)
    await channel.send(embed=embed)    


#----------------------------------------------------------------------------------------------------------------------> Simple "Hello"
@bot.command()
async def Hello(ctx):
    await ctx.send(f"Hello {ctx.message.author.mention}")


#----------------------------------------------------------------------------------------------------------------------> Kick
print(f"Kick command using: ✅")
async def kick(ctx, member : discord.Member):
    try: 
        await member.kick(reason=None)
        await ctx.send("kicked" + member.mention)

    except:
        await ctx.send("I have no right")

#----------------------------------------------------------------------------------------------------------------------> Ground   

print("Group system using: ✅")
@bot.group(name="info")
async def bot_group(ctx):
    await ctx.send("/ban\n/kick\n/nuke\n/moreinfo")

@bot.command()
async def ban(ctx):
    try: 
        await ctx.send(f"Do ban: /ban @user_name")
    
    except:
        await ctx.send("I have no right")

@bot.command()
async def kick(ctx):
    try:
        await ctx.send("Do kick: /kick @user_name")

    except:
        await ctx.send("I have no right")

@bot.command()
async def spoiler(ctx):
    await ctx.send("Do spoiler: /spoiler ")


print("More info using: ✅")
@bot.command(aliases=["help"])
async def moreinfo(ctx, member = None):

    if(member == None):
        member = ctx.author 

    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title="Hi! Its my information book", description="Attention! Use only with the correct rank.", color=discord.Color.from_rgb(17, 31, 47), timestamp=ctx.message.created_at) #dark_embed()
    embed.set_author(name=f"{name}", url="", icon_url=f"{pfp}")

    embed.add_field(name="", value="+---------------------------------------------------------------------------------+", inline=False)

    embed.add_field(name="Commands", value="", inline=False)
    embed.add_field(name="| 1 - Ban |", value="/ban @person_name", inline=True)
    embed.add_field(name="| 2 - Kick person |", value="/kick @person_name", inline=True)
    embed.add_field(name="| 3 - User info |", value="/whois @person_Name", inline=True)
    embed.add_field(name="| 4 - Server info |", value="/server", inline=True)

    embed.add_field(name="",value="+---------------------------------------------------------------------------------+", inline=False)

    embed.add_field(name="Message", value="", inline=False)
    embed.add_field(name="| 4 - Private message |", value="/msg you_user_message", inline=True)
    embed.add_field(name="| 5 - Spoiler |", value="/spoiler you_message", inline=True)

    embed.add_field(name="", value="+---------------------------------------------------------------------------------+", inline=False)
    embed.add_field(name="More:", value="http://kaibot.nhely.hu/", inline=False)
    embed.add_field(name="", value="http://uhusportfolio.nhely.hu/", inline=False)


    await ctx.channel.send(embed=embed)


#----------------------------------------------------------------------------------------------------------------------> User info

print("User info using: ✅")

@bot.command(aliases=["uinfo", "whois"])
async def userinfo(ctx, member : discord.Member=None, usedMember = None):

    if(usedMember == None):
        usedMember = ctx.author 

    roles = [role for role in member.roles]

    embed = discord.Embed(title=f"User info! Used from: {usedMember.name}", color=discord.Color.dark_embed(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar)

    embed.add_field(name="Name: ", value=f"{member.name} #{member.discriminator}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Nickname:", value=f"{member.display_name}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="ID: ", value=f"{member.id}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Status: ", value=f"{member.status}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Created at: ", value=f"{member.created_at}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Joined at: ", value=f"{member.joined_at}", inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name=f"Roles: ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Top role: ", value=member.top_role.mention, inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Bot? ", value=member.bot, inline=False)
    

    await ctx.send(embed=embed)

#----------------------------------------------------------------------------------------------------------------------> Server info
    
@bot.command(aliases=["sinfo", "server"])
async def serverinfo(ctx):

    embed = discord.Embed(title=f"Hi Its {ctx.guild.name} (Server) information book. Used from", color=discord.Color.dark_embed(), timestamp=ctx.message.created_at)

    embed.add_field(name="Created at: ", value=ctx.guild.created_at, inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Members & Bot(s)", value=ctx.guild.member_count, inline=False)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Channels :", value=f"{len(ctx.guild.text_channels)} text channel | {len(ctx.guild.voice_channels)} voice channel")

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Owner: ", value=ctx.guild.owner.name)

    embed.add_field(name="", value=f"------------------------------------------------------------------", inline=False)
    embed.add_field(name="Roles: ", value=len(ctx.guild.roles), inline=False)

    await ctx.send(embed=embed)

    


#----------------------------------------------------------------------------------------------------------------------> Kai run
print()
bot.run("")