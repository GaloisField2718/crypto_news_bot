# Crypto News BOT

This is the repo for the IRCNews bot on telegram (`@ircnews_bot`), which is available on the channel [IRC Crypto News](https://t.me/+_R3hTVETulJmZGM0). 


I'm using [`pipenv`](https://pipenv.pypa.io/en/latest/installation.html) to manage packages.

## Installation
```sh
pipenv shell
pipenv install --ignore Pipfile
```

To launch bot and `get_group_id.py` you need to copy `.env.example` into a new `.env` file. 
`cp .env.example .env`, then edit `.env` file with your text/code editor. 
To get your Token ID contact @BotFather on Telegram.

I made a small script to get the group ID of the chat. Into the virtual environment: `python get_group_id.py`

## Run the bot

Exit the virtual env of root folder. 

Go into: `cd v1`

Copy `cp .env.example .env` and fill `.env` file. 

```
pipenv shell
pipenv install
python main.py
```
