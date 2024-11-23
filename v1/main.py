from src.bot.irc_bot import IRCBot

def main():
    bot = IRCBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        print("\nBot shutting down...")
        bot.telegram.send_message("🔴 IRC Bot is shutting down...")
        bot.die()

if __name__ == "__main__":
    main()
