#coding=utf-8
import telebot
import segno
from data import *

bot = telebot.TeleBot('6947468533:AAH_5sm30S2Qotu7USQNCHxayc5H_POSGZY')
markupA = telebot.types.ReplyKeyboardMarkup()
buttonA = telebot.types.KeyboardButton('Ознакомился')
markupA.row(buttonA)
markupB = telebot.types.ReplyKeyboardMarkup()
buttonB = telebot.types.KeyboardButton('/start')
markupB.row(buttonB)

@bot.message_handler(commands=['start'])
def start(message):
    user_reg(message.from_user.id)
    bot.send_message(message.chat.id, "Привет, это видео инструкция. Первое видео - как поворачивать катаясь - Поворот цапли.", reply_markup=markupA)
    video = open('one.mp4', 'rb')
    bot.send_video(message.chat.id, video=video)
    bot.register_next_step_handler(message, tstep)

def tstep(message):
    bot.send_message(message.chat.id, "Второе видео - как разворачиваться на месте - Робот Вертер.")
    video = open('verter.MOV', 'rb')
    bot.send_video(message.chat.id, video)
    bot.register_next_step_handler(message,trstep)

def trstep(message):
    bot.send_message(message.chat.id, "Будте аккуратны, внимательно прочитайте правила безопасности:")
    photo = open('rules.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.register_next_step_handler(message, fstep)

def fstep(message):
    bot.send_message(message.chat.id, "Вот ваш допуск, покажите его стюарду:")
    qrcode = segno.make_qr(message.from_user.id)
    qrcode.save(f"{message.from_user.id}.png")
    photo = open(f"{message.from_user.id}.png", 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Подписывайтесь, на канал первого в мире велоэллипса, чтобы сделать эллик лучше\nhttps://t.me/+dvijtech", reply_markup=markupB)
    
    
    
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
