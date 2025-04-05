from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from ...ml_module import get_embeddings, create_top
import datetime
import random
import enum
import logging
import typing

class Gamemodes(enum.StrEnum):
    WORD_DAY = 'word_day'
    RANDOM = 'random'
    CUSTOM = 'custom'


async def game_start(gamemode):
    print('GAME START')
    if gamemode == Gamemodes.WORD_DAY:
        print(f'GAME MODE')
        random.seed(int(datetime.datetime.today().toordinal())%233000)
        word_to_play = random.choice(list(get_embeddings().items()))
    elif gamemode == Gamemodes.RANDOM:
        random.seed(None)
        word_to_play = random.choice(list(get_embeddings().items()))
    elif gamemode == Gamemodes.CUSTOM:
        word_to_play = gamemode
    else:
        logging.error(f'error: {gamemode}')

    words_top = create_top(word_to_play)
    return word_to_play, words_top


async def process_guess(update: Update, context: CallbackContext):
    guess = update.message.text.strip()
    words_top: dict = context.user_data['top']
    user_guesses: list = context.user_data.get('user_guesses', [])

    if any(g['word'] == guess for g in user_guesses):
        await update.message.reply_text(f'Слово {guess} уже пробовали.')
        return

    try:
        guess_rating = words_top[guess]
    except KeyError:
        await update.message.reply_text('Почитайте правила ещё раз, пожалуйста.')
        return
    except Exception as e:
        logging.error(f'Error while processing guess: {e!r}')
        await update.message.reply_text('Произошла ошибка. Попробуйте снова.')
        return

    user_guesses.append({'word': guess, 'rating': guess_rating})
    context.user_data['user_guesses'] = user_guesses

    if guess_rating == 0:
        context.user_data['is_playing'] = False
        await update.message.reply_text(f'КРАСАВА, СЛОВО БЫЛО: {guess}')
        return

    recent_guess = f"{guess}: {guess_rating}"
    previous_guesses = sorted(user_guesses[:-1], key=lambda x: x['rating'])[:10]
    formatted_previous = '\n'.join([f'{g["word"]}: {g["rating"]}' for g in previous_guesses])

    reply = f"{recent_guess}\n\n{formatted_previous}"
    await update.message.reply_text(reply)
