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

## Project Structure

```
src/
├── bot/
│   ├── irc_bot.py          # Main IRC bot implementation
│   └── message_handler.py   # Message processing and keyword detection
├── config/
│   ├── keywords.py         # List of crypto-related keywords
│   └── settings.py         # Environment and configuration settings
└── services/
    ├── telegram.py         # Telegram messaging service
    ├── news_cache.py       # Duplicate detection service
    ├── digest_service.py   # Periodic news digest generation
    └── ai_summary_service.py # OpenAI-powered news summarization

# Root level files
├── main.py                 # Application entry point
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── Pipfile               # Python dependencies
├── Pipfile.lock          # Locked dependencies
├── .env                  # Environment variables (not in git)
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## Docker Setup

### Prerequisites
- Docker Desktop installed and running
- Docker Compose installed

### Running with Docker
1. Build and start the container:
```bash
docker-compose up
```

2. Stop the container:
```bash
docker-compose down
```

### Docker Commands Reference
- Rebuild the container after changes:
```bash
docker-compose up --build
```

- View container logs:
```bash
docker-compose logs
```

- Access container shell:
```bash
docker-compose exec irc-bot bash
```

### Troubleshooting
- If you encounter credential issues, try:
```bash
docker login
```

- To reset Docker configuration:
```bash
docker-compose down -v
```

### Docker Files
- `Dockerfile`: Contains the container configuration
- `docker-compose.yml`: Defines the services, networks, and volumes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](../LICENSE) file for details.

Copyright (C) 2024 GaloisField

