from .. import app_config
from .modules import start
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from .modules import text_message_handler
from .modules import choice_custom, choice_random, choice_word_day

def create_bot_application():
    """Sets up the bot with all the necessary handlers."""
    app_config.configure_logging()

    application = ApplicationBuilder().token(app_config.TELEGRAM_BOT_TOKEN).build()
    
    # Register common handlers
    application.add_handler(CommandHandler('start', start))

    application.add_handler(MessageHandler(filters.TEXT, text_message_handler))

    application.add_handler(CallbackQueryHandler(choice_word_day, pattern='^gamemode->word_day$'))
    application.add_handler(CallbackQueryHandler(choice_custom, pattern='^gamemode->custom$'))
    application.add_handler(CallbackQueryHandler(choice_random, pattern='^gamemode->random$'))



    return application


