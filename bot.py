import telebot
from telebot import types
import datetime

from visual import getInfo

tb = telebot.TeleBot()

keyboard = types.InlineKeyboardMarkup()
key_today = types.InlineKeyboardButton(text='Cегодня', callback_data='today')
key_yestoday = types.InlineKeyboardButton(text='Вчера', callback_data='yestoday')
key_week = types.InlineKeyboardButton(text='Неделя', callback_data='week')
key_month = types.InlineKeyboardButton(text='Месяц', callback_data='month')
key_start = types.InlineKeyboardButton(text='С начала', callback_data='start')
keyboard.add(key_today, key_yestoday, key_week, key_month, key_start)

# keyboard_devices = types.InlineKeyboardMarkup()
#
# key_1 = types.InlineKeyboardButton(text='1', callback_data='1')
# key_2 = types.InlineKeyboardButton(text='2', callback_data='2')
# key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
# key_all = types.InlineKeyboardButton(text='all', callback_data='all')
# keyboard_devices.add(key_1, key_2, key_3, key_all)
#

@tb.message_handler(commands=['hi', 'help'])
def send_welcome(message):
    if message.text == "/hi":
        print(message)
        tb.send_message(message.chat.id, text="Период", reply_markup=keyboard)
    elif message.text == "/help":
        tb.send_message(message.chat.id, "Напиши /hi")
    else:
        tb.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")


@tb.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "today":

        currentdate = datetime.datetime.today()
        newdate = currentdate.replace(hour=0, minute=0, second=0, microsecond=0)
        msg = getInfo(newdate, currentdate, '2')
        photo = open('my_plot.png', 'rb')
        tb.send_photo(call.message.chat.id, photo)
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

    elif call.data == "yestoday":
        currentdate = datetime.datetime.today() - datetime.timedelta(days=1)
        start = currentdate.replace(hour=23, minute=59, second=59, microsecond=599999)
        newdate = currentdate.replace(hour=0, minute=0, second=0, microsecond=0)
        msg = getInfo(newdate, start)
        photo = open('my_plot.png', 'rb')
        tb.send_photo(call.message.chat.id, photo)
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

    elif call.data == "week":
        currentdate = datetime.datetime.today() - datetime.timedelta(days=7)
        start = currentdate.replace(hour=23, minute=59, second=59, microsecond=599999)
        newdate = currentdate.replace(hour=0, minute=0, second=0, microsecond=0)
        msg = getInfo(newdate, start)
        photo = open('my_plot.png', 'rb')
        tb.send_photo(call.message.chat.id, photo)
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

    elif call.data == "month":
        currentdate = datetime.datetime.today() - datetime.timedelta(days=30)
        start = currentdate.replace(hour=23, minute=59, second=59, microsecond=599999)
        newdate = currentdate.replace(hour=0, minute=0, second=0, microsecond=0)
        msg = getInfo(newdate, start)
        photo = open('my_plot.png', 'rb')
        tb.send_photo(call.message.chat.id, photo)
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

    elif call.data == "start":
        currentdate = datetime.datetime.today() - datetime.timedelta(days=365)
        start = currentdate.replace(hour=23, minute=59, second=59, microsecond=599999)
        newdate = currentdate.replace(hour=0, minute=0, second=0, microsecond=0)
        msg = getInfo(newdate, start)
        photo = open('my_plot.png', 'rb')
        tb.send_photo(call.message.chat.id, photo)
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

    else:
        msg = 'nithing'
        tb.send_message(call.message.chat.id, msg)
        tb.send_message(call.message.chat.id, text='Выбери период', reply_markup=keyboard)

tb.polling(none_stop=True, interval=0)
