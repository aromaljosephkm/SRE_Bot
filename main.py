import telebot
import json
import time

API_KEY = '1822998997:AAF5S04YLJYodgheGqJo87ZgYkR4h6XdDgo'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(func=lambda message: True)
def checkRoll(message):
    text = ' '
    message_text = message.text.split(' ')

    if 'mentor_help' in message_text or '/start' in message_text:
        bot.reply_to(message,
                     "SRE Mentor Bot Control Statements"
                     "\nmentor_help ==> Help"
                     "\nname_update <name> ==> Register your name with user"
                     "\nmy_update <update> ==> Update your scrum"
                     "\nto_mentor <message> ==> To send this message to Mr. Vivek K C"
                     "\ndev_com <issue faced> ==> To report to Developer")

    elif message_text[0] == 'name_update':
        if len(message_text) > 1:
            name_file = open('names.txt', 'a')
            text = text.join(message_text[1:])
            name = message.from_user.username
            bot.reply_to(message, "Your name has been updated!\nThank You!")
            name_file.write('"'+str(name)+'" :')
            name_file.write('"'+text+'",')
            name_file.close()
        else:
            bot.reply_to(message, "Hey! You forgot to mention your name\nTry again")

    elif message_text[0] == 'my_update':
        if len(message_text) > 1:
            update_file = open('update.txt', 'a')
            text = text.join(message_text[1:])
            name = message.from_user.username
            name_file = open('names.txt', 'r')
            names = name_file.read()
            name_file.close()
            names = names[:-1]
            names = '{' + names + '}'
            name_dict = json.loads(names)
            for key, value in name_dict.items():
                if name == key:
                    name = value
                    t = time.ctime()
                    update_file.write(str(t)+'  :  ')
            update_file.write(name+' ==> ')
            update_file.write(text+'\n')
            update_file.close()
            bot.reply_to(message, "Your update has been noted and attendance is marked!\nThank You!")
            '''if message.from_user.username == name:
                bot.reply_to(message, "Can't be updated as you have not updated your name")'''
        else:
            bot.reply_to(message, "Hey! You forgot to mention your update\nTry again")
    elif message_text[0] == 'to_mentor':
        bot.reply_to(message, "Feature is not yet available!")
    elif message_text[0] == 'dev_com':
        # bot.send_message(609830051, message)
        bot.reply_to(message, "Feature is on progress!")
        bot.reply_to(message, "Feedback sent!\nThank you")
    else:
        bot.reply_to(message, "I am not grown up yet to understand all the things you send!\nSorry! Bear with me and Try again")


bot.polling()
