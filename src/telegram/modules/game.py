from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def choice_custom(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    context.user_data['is_sending_word'] = True

    await query.edit_message_text('Давай слово сюда')



async def start_game_custom(update: Update, context: CallbackContext):
    if context.user_data['']
    custom_text = update.message.text

    if custom_text not in embeddings.keys():
        await update.message.edit_text('Другое слово напиши')

    if len(custom_text.split()) > 1:
        await update.message.edit_text('Одно слово')
    
    context.user_data['is_sending_word'] = False
    