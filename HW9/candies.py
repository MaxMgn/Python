import telebot
# from telebot import types
import random
bot = telebot.TeleBot("5613077244:AAE9_HLBAIDwtdAd7U7LXDwLWO0XsmjS25Y")

candies = 221
max_candies = 28

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Приветствую вас в игре!")
    flag = random.choice(["user", "bot"])
    bot.send_message(message.chat.id, f"Всего в игре {candies} конфет")
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы") # отправка сообщения (кому отправляем, что отправляем(str))
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
    controller(message)

def controller(message):
    global flag
    if candies > 0 :
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_candies}")
            bot.register_next_step_handler(message,player_move)
        else:
            computer_move(message)
    else: 
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id,f"Победил  {flag}! ")

def computer_move(message):
    global candies, flag
    if candies <= max_candies:
        number_to_take = candies
    elif candies % max_candies == 0:
        number_to_take = random.randint(1, max_candies)
    else:
        number_to_take = candies % (max_candies + 1)
        candies -= number_to_take
    bot.send_message(message.chat.id, f"бот взял {number_to_take} конфет")
    bot.send_message(message.chat.id, f"осталось {candies}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)


def player_move(message):
    global candies, flag
    number_to_take = 0
    while (number_to_take < 1 or number_to_take > 28 or number_to_take > candies):
        number_to_take = int(message.text)
        bot.send_message(message.chat.id, f"игрок пытается взять {number_to_take}")
    candies -= number_to_take
    bot.send_message(message.chat.id, f"осталось {candies}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)
    
bot.infinity_polling()

# def player_move ():   
#     number_to_take = 0
#     while (number_to_take < 1 or number_to_take > 28 or number_to_take > candies):
#         number_to_take = input("insert candies number to take: ")
#     return number_to_take

# def computer_move (candies):
#     number_to_take = candies %  29
#     if (number_to_take == 0):
#         number_to_take = randint(1, 28)
#     print ("computer took: " + str(number_to_take))
#     return number_to_take

# candies = 221
# while True:
#     print ("candies left: " + str(candies))
#     candies = candies - player_move ()
#     if candies == 0:
#         print ("player win")
#         break
#     print ("candies left: " + str(candies))
#     candies = candies - computer_move (candies)
#     if candies == 0:
#         print ("computer win")
#         break