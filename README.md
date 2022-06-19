# EVGA-TW-STOCK-Discord-Bot


## Usage
### 1.from source code
1. Install dependencies - `python3 -m pip install -r requirements.txt`

>安裝依賴 - `python3 -m pip install -r requirements.txt`

2. Modify main.py file 

>修改 main.py 檔案

3. Run the program - `python3 main.py` 

>執行程式 `python3 main.py` 

### 2.from docker(not tested)
1. clone the repository to local
2. rename .env(example) to .env
3. change `BOT_TOKEN` and `CHANNEL_ID` to yours
4. docker build
  `docker -t {image_name}:{tag} .` remember to change {image_name} & {tag}
5. docker run
  `docker run --rm {image_name}:{tag}`
6. docker compose (optional, if you don't want to use docker run)
```
#open
docker-compose up      #close termainl = close bot
docker-compose up -d   #detach mod you can close terminal

#log
docker-compose log -f  #see the bot log

#close the bot when you use detach mod
docker-compose down
```
##### notice step 4 5 6 must open the terminal within the repository folder

## Configuration
### rename .env(example) to .env


```python
BOT_TOKEN=ABCDEFG                #discord bot token
CHANNEL_ID=000000000000000000    #要讓機器人發送消息的頻道ID
```

### How to get
[channel id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

[Bot Token](https://www.writebots.com/discord-bot-token/)