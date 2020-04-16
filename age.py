import datetime

age = input('Здравствуйте, введите ваш возраст: ')
year_to = input('Введите год для которого вы хотите узнать ваш возраст: ')

def check_year(age):
	list_year = [1,2,3,4]
	check = age % 10
	if check in list_year:
		if check == 1:
			result = 'год'
		else:
			result = 'года'
	else:
		result = 'лет'
	return result			

now = datetime.datetime.now().year
if int(year_to) > now:
	age_new = int(age)+(int(year_to)-now)
	year_str = check_year(age_new)
	print('Ваш возраст в '+year_to+' году будет '+ str(age_new)+ ' '+year_str+'.')
elif int(year_to) == now:
	year_str = check_year(int(year_to))
	print('Ваш возраст в '+year_to+' году '+ str(age_new)+ ' '+year_str+'.')
else:
	if int(year_to) < now and int(year_to)>= now - int(age):
		age_new = int(age)-(now-int(year_to))
		if age_new == 0:
			print('Вы родились в '+year_to+' году.')
		else:
			year_str = check_year(int(age_new))
			print('Ваш возраст в '+year_to+' году был '+ str(age_new)+ ' '+year_str+'.')
	else:
		print('Ошибка введите правильный год')





