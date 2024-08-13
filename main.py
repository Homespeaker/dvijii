#coding=utf-8
import telebot
import qrcode
from data import *  

bot = telebot.TeleBot('6182241691:AAFl3lahEdNLQGp3hurvMI8JeYbAIRlHc54')

@bot.message_handler(commands=['start'])
def start(message):
    user_reg(message.from_user.id)
    bot.send_message(message.chat.id, "Привет, это видео инструкция. Первое видео - как поворачивать катаясь - Поворот цапли.")
    video = open('tsaplya.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    bot.next_step_handler(message, step2)

def 2step(message):
    bot.send_message(message.chat.id, "Второе видео - как разворачиваться на месте - Робот Вертер.")
    video = open('verter.MOV', 'rb')
    bot.send_video(message.chat.id, video)
    bot.next_step_handler(message, step3)

def 3step(message):
    bot.send_message(message.chat.id, "Будте аккуратны, внимательно прочитайте правила безопасности:")
    photo = open('rules.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.next_step_handler(message, step4)

def 4step(message):
    bot.send_message(message.chat.id, "Вот ваш допуск, покажите его стюарду:")
    data = f"{message.from_user.id}"
    filename = f"{message.from_user.id}.png"
    img = qrcode.make(data)
    bot.send_photo(message.chat.id, img)
    img.save(filename)
    
    
    
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
