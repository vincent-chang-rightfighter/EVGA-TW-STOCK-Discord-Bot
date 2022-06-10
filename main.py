import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
from requests import session

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

# payload = {"ctl00$LFrame$prdList$chkOnlyInStock": "on"}


bot = commands.Bot(command_prefix='-')
channel_id = 000000000000000000


@bot.event
async def on_ready():
    print('Now Login：', bot.user)
    game = discord.Game('EVGA_TW_SITE')
    await bot.change_presence(activity=game, status=discord.Status.online)


async def on_command_error(ctx, error):
    if ctx.channel.id == channel_id:
        if isinstance(error, commands.CommandOnCooldown):
            print("cooldown")
            cd = round(error.retry_after)
            minutes = str(cd // 60)
            seconds = str(cd % 60)
            coolmsg = f"**CD時間**,稍後 {minutes} 分 {seconds} 秒再試"
            # .format(minutes, seconds)
            await ctx.send(coolmsg)
    else:
        await ctx.send("")


# @bot.event

@bot.command()
@commands.cooldown(1, 1200, commands.BucketType.guild)
async def EVGA(ctx):
    if ctx.message.channel.id == channel_id:
        print("run commmand")
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        # embed.set_image(url="https://i.imgur.com/1BFkJ8O.gif")
        embed2 = discord.Embed()
        embed2.colour = discord.Colour.dark_green()
        embed2.set_image(url="https://i.imgur.com/1BFkJ8O.gif")
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

        payload = {"ctl00$LFrame$prdList$chkOnlyInStock": "on"}
        # msg = ""
        i = 0

        with session() as c:
            c.post("https://tw.evga.com/Products/ProductList.aspx?type=0",
                   headers=headers, data=payload)
            res = c.get(
                "https://tw.evga.com/Products/ProductList.aspx?type=0", headers=headers)
            soup = BeautifulSoup(res.text, 'lxml')
            for item in soup.find_all("div", class_="main-product"):
                for product in item.find_all(class_="grid-item-outer"):
                    if product.find(class_="pl-grid-buttons"):
                        model_name = product.find(
                            title="View Details").get_text()
                        model_name_split = model_name.split(", ")
                        if i < 14:
                            # print(i)
                            embed.add_field(name=model_name_split[0]+"\nNT$ "+product.find(class_="pl-grid-price").strong.get_text(
                            ), value="https://tw.evga.com"+product.find(title="View Details").get('href'), inline=False)
                            i += 1
                            print(len(embed))
                        elif i >= 14:
                            # print(i)
                            embed2.add_field(name=model_name_split[0]+"\nNT$ "+product.find(class_="pl-grid-price").strong.get_text(
                            ), value="https://tw.evga.com"+product.find(title="View Details").get('href'), inline=False)
                            i += 1
                            print(len(embed2))

        embed2.timestamp = datetime.now(timezone(timedelta(hours=+8)))
        embed2.set_footer(text='Powered by vinc#5485',
                          icon_url='https://raw.githubusercontent.com/vincent-chang-rightfighter/DiscordWebhook-InstagramUrl/main/icon.png')
        # print(len(embed))
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)

    else:
        print("pass")
        print(ctx.message.channel.id)

bot.run('YOUR Discord bot tokem')
