import telebot
from telebot import types

bot = telebot.TeleBot('6660978182:AAFeqCyyUTh94foSdXwSL3RQwCC2flaSDCw')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Хочешь заработать свой первый миллион?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Да!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Драг металлы')
        btn2 = types.KeyboardButton('Акции')
        btn3 = types.KeyboardButton('Крипта')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Сколько вы готовы вложить?', reply_markup=markup)
        money = message.text
        while money > 0:
            bot.send_message(message.from_user.id, '❓ Во что вкладываемся?', reply_markup=markup) #ответ бота


    elif message.text == 'Драг металлы':
        print(money)
        bot.send_message(message.from_user.id, 'Покупай золото, ежжи, золотой зуб даю!', parse_mode='Markdown')

    elif message.text == 'Акции':
        bot.send_message(message.from_user.id, 'На русский рынок сейчас лучше не выходить...', parse_mode='Markdown')

    elif message.text == 'Крипта':
        bot.send_message(message.from_user.id, 'Биток и эфир бери ежжи', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
