import telebot

from packege.parser import fortnite, CSGO

bot= telebot.TeleBot('1360131281:AAFC1IwsXys5WrgtMfP4PhBxSdmvviGcDVM')
keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard.row("/start")

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    if user.username == 'dodikovich':
        bot.send_message(message.chat.id, 'Бог создал горы, Бог создал деревья, Бог создал тебя, но все мы совершаем ошибки.')
    else:
        IKeybord = telebot.types.InlineKeyboardMarkup()
        FORTNITE = telebot.types.InlineKeyboardButton("Fortnite", callback_data="Fortnite")
        APEX = telebot.types.InlineKeyboardButton("Apex Legends", callback_data="APEX")
        CSGO = telebot.types.InlineKeyboardButton("CSGO", callback_data="CSGO")
        VALORANT = telebot.types.InlineKeyboardButton("Valorant", callback_data="Valorant")
        IKeybord.add(FORTNITE, CSGO, VALORANT, APEX)
        bot.send_message(message.chat.id, 'Привет '+user.first_name+' , выбери игру', reply_markup=IKeybord)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Fortnite':
                bot.send_message(call.message.chat.id, 'Fortnite')
                bot.send_message(call.message.chat.id, 'Send your nickname')

                @bot.message_handler(content_types=['text'])
                def send_text(message):
                    name = message.text
                    bot.send_message(message.chat.id, "it can take several minutes")
                    if name:
                        fortnite(name, bot, message)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Game:",
                                      reply_markup=None)
            elif call.data == 'APEX':
                bot.send_message(call.message.chat.id, 'APEX')
            elif call.data == 'CSGO':
                bot.send_message(call.message.chat.id, 'CSGO')
                bot.send_message(call.message.chat.id, 'Send your steam id\n(Instruction how to discover it:https://support.ubisoft.com/en-gb/Article/000060565 )')

                @bot.message_handler(content_types=['text'])
                def send_text(message):
                    name = message.text
                    bot.send_message(message.chat.id, "it can take several minutes")
                    if name:
                        CSGO(name, bot, message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Game:",
                                      reply_markup=None)
            elif call.data == 'Valorant':
                bot.send_message(call.message.chat.id, 'Valorant')
                bot.send_message(call.message.chat.id, 'Send your nickname')


    except Exception as e:
        print(repr(e))





bot.polling()