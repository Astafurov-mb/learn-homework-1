"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import Config

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def say_hello(update, context):
    update.message.reply_text ('Здарова!')
    print(update)
    print(context)
    update.message.first_name

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('ДАННОЕ СООБЩЕНИЕ (МАТЕРИАЛ) СОЗДАНО И (ИЛИ) РАСПРОСТРАНЕНО ИНОСТРАННЫМ СРЕДСТВОМ МАССОВОЙ ИНФОРМАЦИИ, ВЫПОЛНЯЮЩИМ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА, И (ИЛИ) РОССИЙСКИМ ЮРИДИЧЕСКИМ ЛИЦОМ, ВЫПОЛНЯЮЩИМ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА \n\n\n' + user_text)

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(Config.API_KEY, use_context=True)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start', say_hello))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('стартуем!')
    mybot.start_polling()
    mybot.idle()

main()
