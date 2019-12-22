from datetime import date, time, datetime, timedelta
from glob import glob
import logging
from random import choice

from utils import *

import ephem

def greet_user(bot, update, user_data):
    emoji = get_user_emoji(user_data)
    text = 'Привет {}'.format(emoji)
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(bot, update, user_data):
    emoji = get_user_emoji(user_data)
    user_text = 'Привет, {} {}! Ты написал: {}'.format(update.message.chat.first_name, emoji, update.message.text) 
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text, reply_markup=get_keyboard())


def check_planet(bot,update, user_data):
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    user_question = '{}'.format(update.message.text)
    planet = user_question.split.capitalize()
    date = datetime.now()
    if planet[1] in planet_list:
        place = ephem.planet[1](date)
        constellation = ephem.constellation(place)
        answer = f'Планета {planet} прямо сейчас находится в созвездии {constellation}'
        update.message.reply_text(answer)
    else:
        update.message.reply_text('Проверьте название введенной планеты')

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())

def change_avatar(bot, update, user_data):
    if 'emoji' in user_data:
        del user_data['emoji']
    emoji = get_user_emoji(user_data)
    update.message.reply_text('Готово: {}'.format(emoji), reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Семь дней {}'.format(get_user_emoji(user_data)), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Вот ты и попался {}'.format(get_user_emoji(user_data)), reply_markup=get_keyboard())