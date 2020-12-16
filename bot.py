import telebot

from packege.parser import fortnite

bot= telebot.TeleBot('1360131281:AAFC1IwsXys5WrgtMfP4PhBxSdmvviGcDVM')
keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard.row("/start")

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    if user.username == 'dodickovich':
        bot.send_message(message.chat.id, 'Ты лох по жизни.\nНе хочу в мафию\n')
    else:
        IKeybord = telebot.types.InlineKeyboardMarkup()
        FORTNITE = telebot.types.InlineKeyboardButton("Fortnite", callback_data="Fortnite")
        APEX = telebot.types.InlineKeyboardButton("Apex Legends", callback_data="APEX")
        CSGO = telebot.types.InlineKeyboardButton("CSGO", callback_data="CSGO")
        VALORANT = telebot.types.InlineKeyboardButton("Valorant", callback_data="Valorant")
        IKeybord.add(FORTNITE, CSGO, VALORANT, APEX)
        bot.send_message(message.chat.id, 'Привет '+user.first_name+' , ты написал мне /start', reply_markup=IKeybord)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Fortnite':
                bot.send_message(call.message.chat.id, 'Fortnite')
            elif call.data == 'APEX':
                bot.send_message(call.message.chat.id, 'APEX')
            elif call.data == 'CSGO':
                bot.send_message(call.message.chat.id, 'CSGO')
            elif call.data == 'Valorant':
                bot.send_message(call.message.chat.id, 'Valorant')
            bot.send_message(call.message.chat.id, 'Send your nickname')

            @bot.message_handler(content_types=['text'])
            def send_text(message):
                name = message.text
                bot.send_message(message.chat.id, "it can take several minutes")
                if name:
                    fortnite(name,bot,message)
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Game:",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))





bot.polling()