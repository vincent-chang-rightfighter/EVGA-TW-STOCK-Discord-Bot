import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import requests
from operator import itemgetter

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

item_list = []
bot = commands.Bot(command_prefix='-')
channel_id = 000000000000000000


async def crawler():
    res = requests.get(
        "https://tw.evga.com/Products/ProductList.aspx?type=0", headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        for item in soup.find_all("div", class_="main-product"):
            for product in item.find_all(class_="grid-item-outer"):
                if product.find(class_="pl-grid-buttons"):
                    model_name = product.find(
                        title="View Details").get_text().split(", ")
                    model_price = product.find(
                        class_="pl-grid-price").strong.get_text().replace(",", "")
                    model_url = "https://tw.evga.com" + \
                        product.find(title="View Details").get('href')
                    model_dic = {
                        'name': model_name[0], 'price': model_price, 'url': model_url}
                    item_list.append(model_dic)
            item_list.sort(key=lambda x: int(itemgetter("price")(x)))
            return "success"
    else:
        return "error"


def check_channel(ctx):
    return ctx.channel.id == channel_id


@bot.event
async def on_ready():
    print('Now Login：', bot.user)
    game = discord.Game('EVGA_TW_SITE')
    await bot.change_presence(activity=game, status=discord.Status.online)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        print("cooldown")
        cd = round(error.retry_after)
        minutes = str(cd // 60)
        seconds = str(cd % 60)
        coolmsg = f"**CD時間**,稍後 {minutes} 分 {seconds} 秒再試"
        # .format(minutes, seconds)
        await ctx.send(coolmsg)


@bot.command()
@commands.check(check_channel)
@commands.cooldown(1, 600, commands.BucketType.guild)
async def EVGA(ctx):
    await ctx.message.add_reaction("\u2705")
    message = await ctx.send(f"載入中...\U0001F6F0")
    if await crawler() is "error":
        await ctx.send("程式或EVGA伺服器異常\u2049\uFE0F")
        item_list.clear()
        print("error")

    else:
        # if len(item_list) > 11 split to two message
        if len(item_list) > 0 and len(item_list) <= 11:
            embed = discord.Embed()
            embed.colour = discord.Colour.dark_green()
            for item in item_list:
                embed.add_field(
                    name=item['name']+"\nNT$ "+item['price'], value=item['url'], inline=False)
            embed.timestamp = datetime.now(timezone(timedelta(hours=+8)))
            embed.set_footer(text='Powered by vinc#5485',
                             icon_url='https://raw.githubusercontent.com/vincent-chang-rightfighter/DiscordWebhook-InstagramUrl/main/icon.png')
            print(len(embed))

            await message.edit(content="存貨列表\U0001F389", embed=embed)
            item_list.clear()
            print("send success,item_list <=11")

        elif len(item_list) > 11:
            embed = discord.Embed()
            embed.colour = discord.Colour.dark_green()
            embed2 = discord.Embed()
            embed2.colour = discord.Colour.dark_green()
            i = 0
            for item in item_list:
                if i <= 11:
                    embed.add_field(
                        name=item['name']+"\nNT$ "+item['price'], value=item['url'], inline=False)
                    i += 1
                elif i > 11:
                    embed2.add_field(
                        name=item['name']+"\nNT$ "+item['price'], value=item['url'], inline=False)
                    i += 1

            embed2.timestamp = datetime.now(timezone(timedelta(hours=+8)))
            embed2.set_footer(text='Powered by vinc#5485',
                              icon_url='https://raw.githubusercontent.com/vincent-chang-rightfighter/DiscordWebhook-InstagramUrl/main/icon.png')
            await message.edit(content="存貨列表\U0001F389", embed=embed)
            await ctx.send(embed=embed2)
            item_list.clear()
            print("send success,item_list >11")

bot.run('YOUR Discord bot tokem')
