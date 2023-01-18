import telebot
from dotenv import load_dotenv
import os
import free_date

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Sun"])
def sun(message):
    bot.send_message(message.chat.id, "Que tal " + free_date.cheap_and_sunny_suggest()+"?!")

@bot.message_handler(commands=["Some_clouds"])
def some_clouds(message):
    bot.send_message(message.chat.id, free_date.cheap_and_some_clouds_suggest()+" pode ser uma boa ideia")

@bot.message_handler(commands=["Rain"])
def rain(message):
    bot.send_message(message.chat.id, "Talvez vocês possam "+free_date.cheap_and_rainny_suggest())

@bot.message_handler(commands=["At_night"])
def night(message):
    bot.send_message(message.chat.id, "Talvez "+free_date.cheap_and_night_suggest()+" pode ser uma boa opção")

@bot.message_handler(commands=["No_money"])
def no_money(message):
    text = """
Como está o tempo por ai?
    /Sun Ensolarado 🌞
    /Some_clouds Algumas nuvens ⛅️
    /Rain Chovendo 🌧
    /At_night É noite 🌜"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["Some_money"])
def some_money(message):
    text = """
    Como está o tempo por ai?
        /Suns Ensolarado 🌞
        /Some_cloudss Algumas nuvens ⛅️
        /Rains Chovendo 🌧
        /At_nights É noite 🌜"""
    bot.send_message(message.chat.id, text)

def verify(message):
    return True

@bot.message_handler(func=verify)
def response(message):
    text = """
Olá, casal!!
Meu trabalho aqui é te ajudar a ter o melhor encontro possível, mas antes eu preciso de algumas informações:

Quanto vocês pretendem gastar?
     /No_money Nenhum dinheiro 💸
     /Some_money Pouco dinheiro 💵
     /Richer_than_richie_rich Bastante 💰
     
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(message, text)

bot.polling()