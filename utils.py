from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from utils import *

import settings

def get_user_emoji(user_data):
    if 'emoji' in user_data:
        return user_data['emoji']
    else:
        user_data['emoji'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emoji']

def get_keyboard():
    contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    location_button = KeyboardButton('Отправить геолокацию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Хатю котика', 'Сменить аватар'],
                                        [contact_button, location_button]
                                       ], resize_keyboard=True
                                      )
    return my_keyboard