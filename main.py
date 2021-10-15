import telebot
import random

bot = telebot.TeleBot('1892156235:AAHghPG4KbJV7FuB1Gp5XcHk37RBCG-RFeQ')

name = ''

@bot.message_handler(content_types=['text'])
def whatshername(message):
    if message.text == '/name':
        bot.send_message(message.from_user.id, "Как ее зовут?")
        bot.register_next_step_handler(message, send_compliment)
    else:
        bot.send_message(message.from_user.id, 'Напиши /name')


def send_compliment(message):  # получаем имя
    global name
    name = message.text
    list_of_adverbs = ['очень', 'самая', 'невероятно', 'сумасшедше', 'совершенно',
                       'незабываемо', 'необыкновенно']
    list_of_adjectives = ['восхитительная', 'обожаемая', 'чудесная',
                          'милая', 'красивая', 'счастливая',
                          'удивительная', 'безупречная', 'шикарная',
                          'незабываемая', 'умная', 'крутая', 'разрывная',
                          'нетривиальная']
    list_of_nouns = ['красотка', 'девушка', 'умница', 'зайка',
                     'звезда', 'рыбка', 'детка', 'самочка']

    curr_pos_adverbs = random.randrange(len(list_of_adverbs))
    curr_pos_adjective = random.randrange(len(list_of_adjectives))
    curr_pos_noun = random.randrange(len(list_of_nouns))

    curr_adverb = str(list_of_adverbs[curr_pos_adverbs])
    curr_adjective = str(list_of_adjectives[curr_pos_adjective])
    curr_noun = list_of_nouns[curr_pos_noun]
    bot.send_message(message.from_user.id, name + ' -' +
                     ' ты ' + curr_adverb +
                     ' ' + curr_adjective + ' ' + curr_noun + ')')
    bot.send_message(message.from_user.id, 'Напиши снова /name')


bot.polling(none_stop=True)
