# import telebot
# from telebot import types

# bot = telebot.TeleBot('')

# # @bot.message_handler(commands = ['start'])
# # def start_message(message):
# #     bot.send_message(message.chat.id, 'Hello, i can /register')

# # @bot.message_handler(commands = ['register'])
# # def register(message):
# #     bot.send_message(message.chat.id, 'Enter your name')
# #     bot.register_next_step_handler(message, read_name)

# # def read_name(message):
# #     name = message.text
# #     bot.send_message(message.chat.id, 'Enter your surname')
# #     bot.register_next_step_handler(message, read_sname, name)

# # def read_sname(message, name):
# #     sname = message.text
# #     bot.send_message(message.chat.id, f'Thank you for registration {name}, {sname}')
    
# # bot.infinity_polling()

# @bot.message_handler(commands = ['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Button of greeting')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, 'Hello i am asistent bot of LevelUp', reply_markup= markup)

# @bot.message_handler(content_types=['text'])
# def text_messages(message):
#     if message.text == 'Button of greeting':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
#         btn1 = types.KeyboardButton('How does the studiing goes')
#         btn2 = types.KeyboardButton('Contacts')
#         btn3 = types.KeyboardButton('about us')
#         markup.add(btn1, btn2, btn3)
#         bot.send_message(message.from_user.id, 'Ask a question', reply_markup= markup)

#     elif message.text == 'How does the studiing goes':
#         bot.send_message(message.from_user.id, 'You can see the information about studiing online by clicking this [link]')

# # And so on...

# bot.infinity_polling()