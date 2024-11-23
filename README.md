# Crypto News BOT

This is the repo for the IRCNews bot on telegram (`@ircnews_bot`), which is available on the channel [IRC Crypto News](https://t.me/+_R3hTVETulJmZGM0). 
# IRC News Bot

A specialized IRC bot designed to monitor crypto-related news from IRC channels and forward them to Telegram. The bot features intelligent message filtering, duplicate detection, and periodic news digests.

## Features

- **Real-time News Monitoring**: Connects to IRC channels and monitors messages in real-time
- **Crypto Keywords Detection**: Filters messages based on an extensive list of crypto-related keywords
- **Telegram Integration**: Forwards relevant news directly to a specified Telegram channel
- **Duplicate Prevention**: Implements smart caching to prevent duplicate news from being shared
- **Periodic Digests**: Generates comprehensive news digests every 6 hours, including:
  - Total number of news items
  - Top trending keywords
  - Complete list of news during the period

## Technical Stack

- Python 3.12
- IRC Bot Framework
- Telegram Bot API
- Docker support
- Pipenv for dependency management

## Configuration

The bot is configured using environment variables:
- IRC server and channel settings
- Telegram bot token and chat ID
- Optional OpenAI API key for AI-powered summaries

## Installation

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your configuration
3. Install dependencies:
```bash
pipenv install
```
## Project

To run the bot please refer to [`v1/README.md`](./v1/README.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

Copyright (C) 2024 GaloisField
