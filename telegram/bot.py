import telebot
import random
from telegram.ext import Updater, CommandHandler
import requests
import re
from bs4 import BeautifulSoup
import time
'''token = '1135445121:AAGHHvf9TDKK5FskETdSnC5fGCGRWUdbleg'
bot = telebot.TeleBot(token)

joke_list=['Видишь, на дороге А нарисована? Это для Александров','Меня зовут Саша, но друзья зовут выпить)','Шла Саша по Шоссе и не нам ее судить']

@bot.message_handler(content_types= ["text"])
def repeat_joke_message(message):
    if message.text == 'Саня':
        message.text = random.choice(joke_list)
        bot.send_message(message.chat.id, message.text)'''

def start(update, context):
  update.message.reply_text('Привет!  Используй /get <категория> чтобы получить ссылку на товар')
  update.message.reply_text('Доступные категории: Телефоны и смарт-часы, Ноутбуки и планшеты, Книги')
def get_random_link(update, context):    
    #chat_id = update.message.chat_id
    category = context.args
    string_category = ' '.join(category)
    category_dict={'Телефоны и смарт-часы':'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/',
                    'Ноутбуки и планшеты':'https://www.ozon.ru/category/noutbuki-planshety-i-elektronnye-knigi-8730/',
                    'Книги':'https://www.ozon.ru/category/knigi-16500/?bymediatype=1147731%2C1167663%2C1147732'}

    if string_category in category_dict:
        link = category_dict[string_category]
        result_list_link = links(link)
        result_link = random.choice(result_list_link)
        update.message.reply_text('https://www.ozon.ru'+str(result_link))          
    else:
        update.message.reply_text('Указанной категории не существует')

    
def links(url):
    result_list_link =[]
    params = {}
    for page in range(1,7):
        params['page'] = page
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72'}
        response=requests.get(url.strip(),headers = headers,params=params)
        soup = BeautifulSoup(response.content, 'html.parser')
        tpl = r'\/context\/\S+'
        with open("result.txt", "a") as file:
            for link in soup.find_all("a"):
                if re.match(tpl, str(link.get("href"))) is not None:
                    if link.get("href") not in result_list_link:
                        file.write('https://www.ozon.ru'+link.get("href")+'\n')
                        result_list_link.append(str(link.get("href")))
    return result_list_link

def main():
    token=''
    updater = Updater(token, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get_random_link))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    #test('https://www.ozon.ru/category/knigi-16500/')
    main()
    #print(links('https://www.ozon.ru/highlight/22872/'))

