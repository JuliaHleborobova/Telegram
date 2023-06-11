
import telebot
from config import token
from telebot import types
import requests
import re
import telebot.callback_data
import datetime


bot = telebot.TeleBot(token)


#dt_now = datetime.datetime.now()


def fun_horo(znak):

    req = requests.get(f'https://horo.mail.ru/prediction/{znak.lower()}/today/')
    goro_text = re.search(
        r'<div class="article__item article__item_alignment_left article__item_html"><p>(.+)</p>\s+<p>(.+)</p>',
        req.text).groups()
    return str(goro_text[0])

#Ф-ция, обрабатывающая команду "/start"

@bot.message_handler(commands=["start"])

def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()  #создаем инлайн-клавиатуру

    # создаем кнопки

    btn1 = types.InlineKeyboardButton(text='♈Овен', callback_data = 'aries')
    btn2 = types.InlineKeyboardButton(text='♉Телец', callback_data ='taurus')
    btn3 = types.InlineKeyboardButton(text='♊Близнецы', callback_data ='gemini')
    btn4 = types.InlineKeyboardButton(text='♋Рак', callback_data ='cancer')
    btn5 = types.InlineKeyboardButton(text='♌Лев', callback_data ='leo')
    btn6 = types.InlineKeyboardButton(text='♍Дева', callback_data ='virgo')
    btn7 = types.InlineKeyboardButton(text='♎Весы', callback_data ='libra')
    btn8 = types.InlineKeyboardButton(text='♏Скорпион', callback_data ='scorpio')
    btn9 = types.InlineKeyboardButton(text='♐Стрелец', callback_data ='sagittarius')
    btn10 = types.InlineKeyboardButton(text='♑Козерог', callback_data ='capricorn')
    btn11 = types.InlineKeyboardButton(text='♒Водолей', callback_data ='aquarius')
    btn12 = types.InlineKeyboardButton(text='♓Рыбы', callback_data ='pisces')


    #заносим кнопки в клавиатуру
    markup_inline.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)

    #выводим сообщение, к которому будут крепиться наши кнопки + прикрепляем кнопки
    bot.send_message(message.from_user.id, "Привет, {0.first_name}! \n Cейчас я расскажу тебе гороскоп на сегодня. Выбери свой знак зодиака".format(message.from_user),
                        reply_markup = markup_inline)


#создадим обработчик обратного запроса
@bot.callback_query_handler(func=lambda callback: callback.data)

def answer(callback):
    if callback.data == 'aries':  # формируем гороскоп
        text = fun_horo(callback.data)

        #bot.send_message(callback.message.chat.id, dt_now)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♈Овен")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())  # фиксировать клавиатуру reply_markup = markup_inline
    elif callback.data == 'taurus':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♉Телец")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'gemini':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♊Близнецы")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'cancer':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♋Рак")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'leo':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♌Лев")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'virgo':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♍Дева")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'libra':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♎Весы")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'scorpio':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♏Скорпион")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'sagittarius':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♐Стрелец")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'capricorn':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♑Козерог")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'aquarius':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♒Водолей")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())
    elif callback.data == 'pisces':
        text = fun_horo(callback.data)
        bot.send_message(callback.message.chat.id, "Ваш знак зодиака - \n ♓Рыбы")
        bot.send_message(callback.message.chat.id, text, reply_markup= types.InlineKeyboardMarkup())


# Запускаем бота
bot.polling(none_stop=True, interval=0)





