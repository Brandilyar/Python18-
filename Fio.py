import random
qualities=['Умный','Доброжелательный','Воспитанный','Пунктуальный','Чистоплотный']


kolvo = int(input('Введите количетсво людей, которое вы хотите добавить: '))
slovar={'name':[],'surname':[]}

for i in range(kolvo):
	name = input('Введите имя человека: ')
	surname = input('Введите фамилию человека: ')
	slovar['name'].append(name.strip().title())
	slovar['surname'].append(surname.strip().title())
for i in range(kolvo):
	qualities_one = random.choice(qualities)
	print(slovar['name'][i]+' '+slovar['surname'][i]+' '+qualities_one)	
