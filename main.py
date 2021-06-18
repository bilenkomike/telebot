import telebot
bot=telebot.TeleBot("1842712437:AAHGT9LW3IJF6BQFIj6nlzk8mI6tgnkWxgI")
"""<--Кнопки-->"""
mainboard=telebot.types.InlineKeyboardMarkup(row_width=2, )
first_button=telebot.types.InlineKeyboardButton(text="Профиль",callback_data="button_prof")
second_button=telebot.types.InlineKeyboardButton(text="Мои логики",callback_data="button_money")
third_button=telebot.types.InlineKeyboardButton(text="Домашнее задание",callback_data="button_homework")
fourth_button=telebot.types.InlineKeyboardButton(text="Мои проекты",callback_data="button_project")
mainboard.add(first_button,second_button,third_button,fourth_button)



bordkeyboard=telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
one_button=telebot.types.KeyboardButton(text="Профиль")
two_button=telebot.types.KeyboardButton(text="Мои логики")
three_button=telebot.types.KeyboardButton(text="Домашнее задание")
four_button=telebot.types.KeyboardButton(text="Мои проекты")
bordkeyboard.add(one_button,two_button,three_button,four_button)
"""<--Регистрациянама-->"""
def regist(call):
    reg=[]
    def onestep(message):
        reg.append(message.text)
        msg = bot.send_message(call.message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg,secondstep)
    def secondstep(message):
        reg.append(message.text)
        bot.send_message(call.message.chat.id, "Имя: "+reg[0]+"\n"+"Фамилия: "+reg[1],reply_markup=bordkeyboard)

    msg=bot.send_message(call.message.chat.id, "Введите имя")
    bot.register_next_step_handler(msg,onestep)

@bot.message_handler(commands=["start"])
def start(commands):
    bot.send_message(commands.chat.id,"Привет! Меня зовут Mike! Я - бот",reply_markup=bordkeyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data=="button_prof":
        regist(call)

@bot.message_handler(content_types=["text"])
def printtext(message):
    text = message.text.split()
    badtext = ['сука','блять','пидор','пиздабол',]

    for textin in text:
        if textin in badtext:
            bot.send_message(message.chat.id, "Another one time you will be banned!!")
        else:
            bot.send_message(message.chat.id,textin)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Профиль':
        bot.send_message(message.chat.id, "Hello guys", reply_markup=mainboard)

bot.infinity_polling()