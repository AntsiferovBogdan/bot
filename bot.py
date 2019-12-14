from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, time, datetime, timedelta
import ephem
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text) 
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def check_planet(bot,update):
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

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', check_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    mybot.start_polling()
    mybot.idle()


main()
