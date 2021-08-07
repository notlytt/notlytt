#Dont forget copy & paste = no learning


@bot.command(aliases=['Clear'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int, ):
    if amount <= 1:
        return await ctx.send(':x:The number is to small! pleas choose a number in between 2-100!')
    else:
        if amount >= 100:
            return await ctx.send(":x:The number is to big! pleas choose a number in between 2-100!")

    await ctx.channel.purge(limit=int(amount))
    await ctx.send(f"{amount} messages got cleared!")
    
@bot.command(aliases=['Ban'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member is None or member == ctx.message.author:
        await ctx.channel.send("You cant ban youreself!")
        return
    await member.ban(reason=reason)
    await ctx.send(f'Banned for  {reason} ')

    
   
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.channel.send('You cant kick  youreself!')

    await member.kick(reason=reason)
    await ctx.send(f'Kicked for {reason}')
    
@bot.command(aliases=['Userinfo'])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    roles = [role for role in member.roles[1:]]

    embed = discord.Embed(colour=member.color, timestap=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="User Id:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Accound createt at:", value=member.created_at.strftime("%d.%m.%Y  "))
    embed.add_field(name="Joined on:", value=member.joined_at.strftime("%d.%m.%Y"))

    msg = ""
    for role in roles:
        msg = msg + f"{role.mention}\n"
    embed.add_field(name=f"Roles ({len(roles)})", value=msg)
    embed.add_field(name="Highest:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)
