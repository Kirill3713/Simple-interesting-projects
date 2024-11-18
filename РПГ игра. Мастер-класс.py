"""ВНИМАНИЕ!!! 99% КОДА ПИСАЛ НЕ Я! ЧТОБЫ КОД СРАБОТАЛ НУЖНО ЗАПУСТИТЬ КОД И ЗАПУСТИТЬ ТЕЛЕГРАММ-БОТА!!!"""
import telebot

TOKEN = '7396988552:AAFtkk4V96WTDIRsz9FVZx8GVdGN9SpymqQ'

bot = telebot.TeleBot(TOKEN)

from pprint import pprint

# Словарь для хранения состояния игр
games = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши /play чтобы начать игру в камень-ножницы-бумага.")


@bot.message_handler(commands=['play'])
def start_game(message):
    chat_id = message.chat.id
    if chat_id not in games:
        games[chat_id] = {
            'player1': message.from_user.id,
            'player1_choice': None,
            'player2': None,
            'player2_choice': None
        }
        bot.reply_to(message, "Ожидание второго игрока. Попросите их написать /join.")
    else:
        bot.reply_to(message, "Игра уже началась в этом чате.")


@bot.message_handler(commands=['join'])
def join_game(message):
    chat_id = message.chat.id
    if chat_id in games:
        bot.reply_to(message, "Вы не можете играть сами с собой. Подождите, пока кто-то другой присоединится.")
        return
    for game_id in games:
        if games[game_id]['player2'] is None:
            games[game_id]['player2'] = chat_id
            bot.reply_to(message,
                         "Вы присоединились к игре! Используйте /choose чтобы выбрать камень, ножницы или бумагу.")
            break
    else:
        bot.reply_to(message, "Нет активной игры для присоединения или уже есть два игрока.")
    pprint(games)


@bot.message_handler(commands=['choose'])
def choose(message):
    text = message.text.split()
    if len(text) < 2:
        bot.reply_to(message, "Используйте команду так: /choose камень, ножницы или бумага.")
        return

    choice = text[1].lower()
    if choice not in ['камень', 'ножницы', 'бумага']:
        bot.reply_to(message, "Неверный выбор. Пожалуйста, выберите камень, ножницы или бумага.")
        return

    chat_id = message.chat.id
    for game_id in games:
        if game_id == chat_id:
            games[game_id]['player1_choice'] = choice
            break
        elif games[game_id]['player2'] == chat_id:
            games[game_id]['player2_choice'] = choice
            break
    bot.reply_to(message, "Вы выбрали " + choice)

    if games[game_id]['player1_choice'] is not None and games[game_id]['player2_choice'] is not None:
        determine_winner(game_id)
    pprint(games)


def determine_winner(chat_id):
    game = games[chat_id]
    player1_choice = game['player1_choice']
    player2_choice = game['player2_choice']

    if player1_choice == player2_choice:
        result = "Ничья!"
    elif (player1_choice == "камень" and player2_choice == "ножницы") or \
            (player1_choice == "ножницы" and player2_choice == "бумага") or \
            (player1_choice == "бумага" and player2_choice == "камень"):
        result = "Победил игрок 1!"
    else:
        result = "Победил игрок 2!"

    bot.send_message(game['player1'], result)
    bot.send_message(game['player2'], result)
    del games[chat_id]  # Закончить игру и очистить состояние


bot.polling()