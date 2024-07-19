import telebot
from data import *  

bot = telebot.TeleBot('6182241691:AAFl3lahEdNLQGp3hurvMI8JeYbAIRlHc54')

@bot.message_handler(commands=['start'])
def start(message):
    user_reg(message.from_user.id)
    bot.send_message(message.chat.id, "Обзор, инструкция, обучение и контакты на этом сайте:\n"
                     "https://ellic.tilda.ws/")
    
@bot.message_handler(commands=['clear_base'])
def clear(message):
    clear_base()
    bot.send_message(message.chat.id, "База очищена")

@bot.message_handler(commands=['create_table'])
def table(message):
    create_datatable()

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - Получить инструкцию к боту")

bot.polling()