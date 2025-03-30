from telegram import Update
from telegram.ext import CallbackContext
from ...ml_module import get_embeddings


async def start_custom_game(update: Update, context: CallbackContext):
    from . import game_start
    text = update.message.text

    if text not in get_embeddings().keys():
        await update.message.edit_text('Другое слово напиши')
        return

    if len(text.split()) > 1:
        await update.message.edit_text('Одно слово')
        return
    
    context.user_data['is_sending_word'] = False
    context.user_data['is_playing'] = True

    word_to_play, top = await game_start(text)

    context.user_data['word_to_play'] = word_to_play
    context.user_data['top'] = top

    update.message.reply_text(
        text='Начинаем'
    )