from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import logging


async def choice_custom(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    context.user_data['is_sending_word'] = True

    await query.edit_message_text('Давай слово сюда')


async def choice_gamemode(update: Update, context: CallbackContext):
    from . import game_start
    from . import fallback
    from . import Gamemodes
    query = update.callback_query
    await query.answer()
    gamemode = query.data.split(':')[1]
    print('EXEC')
    if gamemode == Gamemodes.WORD_DAY:
        print('WORD DAY')
        word_to_play, words_top = await game_start(gamemode)
    elif gamemode == Gamemodes.RANDOM:
        word_to_play, words_top = await game_start(gamemode)
    elif gamemode == Gamemodes.CUSTOM:
        await choice_custom(update, context)
        return
    else:
        logging.error(f'WRONG CALLBACK DATA: {query}')
        await fallback(update, context)
        await query.delete_message()

    context.user_data['word_to_play'] = word_to_play
    context.user_data['top'] = words_top

    logging.info(f'Word to play for user {update.effective_user.username}: {word_to_play}')
    context.user_data['is_playing'] = True
    await query.edit_message_text('Угадывай слово. \n ► Правила таковы: \n⌂ Крутое правило #1\n⌂ Крутое правило #2')