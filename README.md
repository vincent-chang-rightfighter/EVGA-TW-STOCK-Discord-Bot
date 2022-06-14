# EVGA-TW-STOCK-Discord-Bot


## Usage
1. Install dependencies - `python3 -m pip install -r requirements.txt`

>安裝依賴 - `python3 -m pip install -r requirements.txt`

2. Modify main.py file 

>修改 main.py 檔案

3. Run the program - `python3 main.py` 

>執行程式 `python3 main.py` 


## Configuration

### Modify main.py 

#### line 13

Replace to your discord server channel id
>替換成你的伺服氣某頻道id

How to know channel id 
[discord support](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

```py
channel_id = 000000000000000000
```

#### line 110
Change your discord bot token 
>修改你的 discord bot token

[How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/)

```py
bot.run('YOUR Discord bot tokem')
```