from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def choice_custom(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    context.user_data['is_sending_word'] = True

    await query.edit_message_text('Давай слово сюда')
    

async def choice_random(update: Update, context: CallbackContext):
    from . import game_start
    query = update.callback_query
    await query.answer()
    wort_to_play, top = await game_start('RANDOM')

    context.user_data['word_to_play'] = wort_to_play
    context.user_data['top'] = top
    await query.edit_message_text('Давай слово сюда')


async def choice_word_day(update: Update, context: CallbackContext):
    from . import game_start
    query = update.callback_query
    await query.answer()
    wort_to_play, top = await game_start('WORD_GAME')

    context.user_data['word_to_play'] = wort_to_play
    context.user_data['top'] = top

    await query.edit_message_text("lol")