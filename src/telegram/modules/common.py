from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton('Слово дня', callback_data='gamemode->word_day')],
        [InlineKeyboardButton('Свое Слово', callback_data='gamemode->custom')],
        [InlineKeyboardButton('Feel lucky', callback_data='gamemode->random')],
    ]
    
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text='Как выберем слово?',
        reply_markup=markup,
    )


