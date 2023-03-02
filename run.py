import requests
import telebot
import ipaddress

BOT_TOKEN = 'PUT HERE YOUR TOKEN FROM BOT_FATHER'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def hello_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добрый день! Введите корректный IP адрес для получения информации')


@bot.message_handler(content_types=['text'])
def handler_text(message):
    text = message.text
    try:
        test = ipaddress.ip_address(text)
        if test.is_private == True:
            bot.send_message(message.chat.id, 'Данный IP адрес не является внешним!')
        else:
            response = requests.get(url=f'http://ip-api.com/json/{text}').json()
            # print(response)

            data1 = str('IP ' + ': ' + response.get('query'))
            data2 = str('Int prov ' + ': ' + response.get('isp'))
            data3 = str('Org ' + ': ' + response.get('org'))
            data4 = str('Country ' + ': ' + response.get('country'))
            data5 = str('Region Name ' + ': ' + response.get('regionName'))
            data6 = str('City ' + ': ' + response.get('city'))
            data7 = str('ZIP ' + ': ' + response.get('zip'))
            data8 = response.get('lat')
            data88 = str('Lat ' + ': ') + str(data8)
            data9 = response.get('lon')
            data99 = str('Lon ' + ': ') + str(data9)

            result = str(data1+'\n'+data2+'\n'+data3+'\n'+data4+'\n'+data5+'\n'+data6+'\n'+data7+'\n'+data88+'\n'+data99)

            bot.send_message(message.chat.id, result)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный IP адрес!')

bot.polling()
