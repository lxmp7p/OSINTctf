import requests
import telebot
import re
import datetime

point = 0
last_command = [0]
bot = telebot.TeleBot(TOKEN)
scoreboard = [{'id': 0, 'username': 1, 'score': 0, 'accepted': [0]},]
def set_point(state=[]):
    if not state:
        state.append(0)
    state[0] += 1
    return state[-1]

def save_result():
	f = open('scoreboard.txt', 'a')
	f.write(str(scoreboard))
	f.close()

@bot.message_handler(commands=['start'])
def start_message(message):
	have = False
	for i in scoreboard:
		if (i.get('id') == message.chat.id ):
			print("have" + str(scoreboard))
			have = True
			bot.send_message(message.chat.id, 'Добро пожаловать! Выберите таск: \n /1)Название игры \n /2)Учеба \n /3)Работа \n /4)Имя \n /5)Фамилия \n /6)ФИО  \n /7)Номер телефона  \n /8)Во что играл  \n /9 Телефон \n /10)Дополнительная информация    ')
			break
	if (have == False):
		print("add" + str(scoreboard))
		scoreboard.append({'id': message.chat.id, 'username': message.chat.username, 'score': 0, 'accepted':[0]})
		bot.send_message(message.chat.id, 'Добро пожаловать! Выберите таск: \n /1)Название игры \n /2)Учеба \n /3)Работа \n /4)Имя \n /5)Фамилия \n /6)ФИО  \n /7)Номер телефона  \n /8)Во что играл \n /9 Телефон  \n /10)Дополнительная информация    ')



def add_point(message, task_num):
	for i in scoreboard:
		if (i.get('id') == message.chat.id ):
			if (task_num not in i["accepted"]):
				score = i.get('score') + 1
				i["score"] = score
				i['accepted'].append(task_num)
				save_result()
				bot.send_message(message.chat.id, 'Правильно!')
				if (1 in i['accepted'] and 2 in i['accepted'] and 3 in i['accepted'] and 4 in i['accepted'] and 5 in i['accepted'] and 6 in i['accepted'] and 7 in i['accepted'] and 8 in i['accepted'] and 9 in i['accepted'] and 11 in i['accepted']):
					print('-------------------\n' + str(message.chat.id) + str(message.chat.username) + ' РЕШИЛ ВСЕ ТАСКИ!')
			else:
				bot.send_message(message.chat.id, 'Вы уже решили данный таск!')

@bot.message_handler(commands=['11'])
def send_text(message):
	commands = a
	if (commands[-1] == 1):
		if (re.search(r'----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n secret' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил secret таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,11)
			commands = [0]




@bot.message_handler(commands=['scoreboard'])
def start_message(message):
	temp = []
	for i in scoreboard:
		bot.send_message(message.chat.id, 'username: ' + str(i.get("username")) + ' score: ' + str(i.get('score')) + ' accepted:' + str(i.get('accepted')))

@bot.message_handler(commands=['1'])
def start_message(message):
	last_command.append(1)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['2'])
def start_message(message):
	last_command.append(2)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['3'])
def start_message(message):
	last_command.append(3)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['4'])
def start_message(message):
	last_command.append(4)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['5'])
def start_message(message):
	last_command.append(5)
	bot.send_message(message.chat.id, '----')

@bot.message_handler(commands=['6'])
def start_message(message):
	last_command.append(6)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['7'])
def start_message(message):
	last_command.append(7)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['8'])
def start_message(message):
	last_command.append(8)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['9'])
def start_message(message):
	last_command.append(9)
	bot.send_message(message.chat.id, ''----',')

@bot.message_handler(commands=['10'])
def start_message(message):
	last_command.append(10)
	bot.send_message(message.chat.id, '----')

a = last_command
@bot.message_handler(content_types=['text'])
def send_text(message):
	commands = a
	if (commands[-1] == 1):
		if (re.search(r''----',',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 1' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил первый таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,1)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 2):
		if (re.search(r''----',',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 2' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил второй таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,2)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 3):
		if (re.search(r'----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 3' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил третий таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,3)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 4):
		if (re.search(r'----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 4' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил четвертый таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,4)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 5):
		if (re.search(r'----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 5' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил пятый таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,5)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 6):
		if (re.search(r'----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 6' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил шестой таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,6)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 7):
		if (re.search(r''----',message.text) or re.search(r'[+]?[7-8]9313',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 7' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил седьмой таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,7)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 8):
		if (re.search(r''----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 8' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил восьмой таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,8)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

	if (commands[-1] == 9):
		if (re.search(r''----',message.text)):
			point = set_point()
			now = datetime.datetime.now()
			f = open('points/'+str(message.chat.id), 'a')
			f.write('\n 9' + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			f.close()
			print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' решил девятый таск в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
			add_point(message,9)
			commands = [0]
		else:
			bot.send_message(message.chat.id, 'Ответ неверный!')

    
	if (commands[-1] == 10):
		now = datetime.datetime.now()
		f = open('another_info/' + str(message.chat.id), 'a')
		f.write('\n' + message.text + ' Time: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
		f.close()
		print('Username: ' + str(message.chat.username) + ',id: ' + str(message.chat.id) + ' добавил инфу в '  + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
		bot.send_message(message.chat.id, 'Добавлено!')
		commands = [0]


bot.polling()