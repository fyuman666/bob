import argparse
import random
import socket
import threading
import telebot
from telebot import types

ap = argparse.ArgumentParser()
ap.addargument("-i", "--ip", type=str, help="Host ip")
ap.addargument("-p", "--port", type=int, help="Port")
ap.addargument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.addargument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.addargument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parseargs())

ip = args'ip'
port = args'port'
choice = args'choice'
times = args'times'
threads = args'threads'

proxies = 
    "socks5://41.65.103.27:1976",
    "http://89.43.31.134:3128",
    "http://80.190.74.13:8000",
    "http://115.132.32.91:8080",
    "http://15.204.161.192:18080",
    "http://201.91.82.155:3128",
    "http://103.17.77.5:3128",
    "http://43.133.136.208:8800",
    "http://34.154.161.152:80",
    "http://115.127.23.130:8674"


bot = telebot.TeleBot("6229938354:AAH3I0u4httA0ERatlFY1cY_JI-pr8UAtsE", proxy=random.choice(proxies))

@bot.messagehandler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(rowwidth=2)
    btnudp = types.KeyboardButton('UDP Flood')
    btntcp = types.KeyboardButton('TCP Flood')
    markup.add(btnudp, btntcp)
    bot.sendmessage(message.chat.id, "PROTOCOL:", replymarkup=markup)

@bot.messagehandler(func=lambda message: True)
def processmessage(message):
    if message.text == 'UDP Flood':
        bot.sendmessage(message.chat.id, "Введите IP адрес:")
        bot.registernextstephandler(message, getipudp)
    elif message.text == 'TCP Flood':
        bot.sendmessage(message.chat.id, "Введите IP адрес:")
        bot.registernextstephandler(message, getiptcp)
    else:
        bot.sendmessage(message.chat.id, "error")

def getipudp(message):
    global ip
    ip = message.text
    bot.sendmessage(message.chat.id, "Введите PORT:")
    bot.registernextstephandler(message, getportudp)

def getportudp(message):
    global port
    port = int(message.text)
    runthreadedattack('udp')
    bot.sendmessage(message.chat.id, "done")

def getiptcp(message):
    global ip
    ip = message.text
    bot.sendmessage(message.chat.id, "Введите PORT:")
    bot.registernextstephandler(message, getporttcp)

def getporttcp(message):
    global port
    port = int(message.text)
    runthreadedattack('tcp')
    bot.sendmessage(message.chat.id, "done")

def runudpattack():
    # Ваш код для атаки UDP
    pass

def runtcpattack():
    # Ваш код для атаки TCP
    pass

def runthreadedattack(attacktype):
    # Ваш код для многопоточной атаки
    pass

bot.polling()