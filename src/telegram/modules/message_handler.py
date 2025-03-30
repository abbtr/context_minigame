from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def text_message_handler(update: Update, context: CallbackContext):
    from . import start_custom_game
    user_data = context.user_data
    text = update.message.text

    if user_data.get('is_playing'):
        pass
    elif user_data.get('is_sending_word'):
        await start_custom_game(update, context)    
    else:
        await fallback(update, context)


async def fallback(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton('Слово дня', callback_data='gamemode->word_day')],
        [InlineKeyboardButton('Свое Слово', callback_data='gamemode->custom')],
        [InlineKeyboardButton('Feel lucky', callback_data='gamemode->random')],
    ]
    
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text='Сначала нажми на кнопку. Писать пока ничего не просили. Как выберем слово?',
        reply_markup=markup,
    )


        


