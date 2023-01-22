import telebot
from dotenv import load_dotenv
import os
from options import Options
from dates import Dates

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)
options = Options()
dates = Dates()


def suggest_place(message):
    place = dates.getADate(options.getWether(), options.getCosts())

    text = """
SUGESTÃO:
   Talvez """ + place + """ pode ser uma boa opção.


O que acham?
    /Love_it Amei, iremos visitar!
    /Visited Já visitamos este lugar
    /Not_now Não estamos afim de fazer esse passeio agora"""
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["Sun", "Some_clouds", "Rain", "At_night"])
def choose_wether(message):
    option_selected = message.text[1:]
    options.setWether(option_selected)
    suggest_place(message)


@bot.message_handler(commands=["No_money", "Some_money", "Richer_than_richie_rich"])
def choose_costs(message):
    option_selected = message.text[1:]
    options.setCosts(option_selected)
    text = """
Como está o tempo por ai?
    /Sun Ensolarado 🌞
    /Some_clouds Algumas nuvens ⛅️
    /Rain Chovendo 🌧
    /At_night É noite 🌜"""
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
