from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from ...ml_module import get_embeddings, create_top
import datetime
import random

async def game_start(text):
    if text == 'RANDOM':
        word_to_play = random.choice(list(get_embeddings().items()))
    elif text == 'WORD_GAME':
        random.seed(int(datetime.datetime.today().toordinal())%233000)
        word_to_play = random.choice(list(get_embeddings().items()))
    else:
        word_to_play = text

    print(list(get_embeddings().items())[0])
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n', type(word_to_play))
    top = create_top(word_to_play)
    return word_to_play, top
