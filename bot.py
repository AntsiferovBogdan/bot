from datetime import date, time, datetime, timedelta
import logging
from glob import glob
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, 
            MessageHandler, Filters)

import ephem
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


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

def get_user_emoji(user_data):
    if 'emoji' in user_data:
        return user_data['emoji']
    else:
        user_data['emoji'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emoji']

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

def get_keyboard():
    contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    location_button = KeyboardButton('Отправить геолокацию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Хатю котика', 'Сменить аватар'],
                                        [contact_button, location_button]
                                       ], resize_keyboard=True
                                      )
    return my_keyboard

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('planet', check_planet, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('Хатю котика'), send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('Сменить аватар'), change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    
    mybot.start_polling()
    mybot.idle()


main()
