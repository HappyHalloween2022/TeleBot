import telebot
from telebot import types
token = '5982453957:AAGwAVrSeYGNlHpS5tIeY2gbbk4Yv1Wu0i8'

bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Привет, Я мастер перманентного макияжа Алена! ✌️ \nНажми /help")



# @bot.message_handler(commands = ['help'])
# def help_message(message):
#     bot.send_message(message.chat.id, '/start\n/url\n/help!')



# @bot.message_handler(commands = ['url'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn_my_site= types.InlineKeyboardButton(text='Мой Instagram', url='https://instagram.com/alena.browart?igshid=YmMyMTA2M2Y=')
#     markup.add(btn_my_site)
#     bot.send_message(message.chat.id, "Нажми на кнопку и перейди в мой Instagram! (не забудь включить VPN)", reply_markup = markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Группа в ВК')
        btn2 = types.KeyboardButton('Мой Instagram')
        btn3 = types.KeyboardButton('Запись на процедуры')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Группа в ВК':
        bot.send_message(message.from_user.id, 'https://vk.com/club212545325')

    elif message.text == 'Мой Instagram':
        bot.send_message(message.from_user.id, 'https://instagram.com/alena.browart?igshid=YmMyMTA2M2Y=')

    elif message.text == 'Запись на процедуры':
        bot.send_message(message.from_user.id, 'https://api.whatsapp.com/send?phone=79258535745&text=%D0%94%D0%BE%D0%B1%D1%80%D1%8B%D0%B9+%D0%B4%D0%B5%D0%BD%D1%8C%2C+%D0%90%D0%BB%D1%91%D0%BD%D0%B0+%F0%9F%A4%8E%D0%A5%D0%BE%D1%87%D1%83+%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F+%D0%BD%D0%B0+%D0%B1%D1%80%D0%BE%D0%B2%D0%BA%D0%B8%2C+%D0%BF%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D0%B6%D0%B8%D1%82%D0%B5+%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BE%D1%88%D0%BA%D0%B8')

bot.infinity_polling()