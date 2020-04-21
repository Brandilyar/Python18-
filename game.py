from random import randint
def check_raz(raz):
	list_raz = [1,2,3,4]
	check = raz % 10
	if check in list_raz:
		if check == 1:
			result = 'разряд'
		else:
			result = 'разряда'
	else:
		result = 'разрядов'
	return result			
def check_pod(pod):
	return pod+1
print('Здравствуйте, угадайте загаданное число')
kolvo_raz = input('Введите максимальное количество разрядов числа: ')
rand_dapozon=randint(0, 10**int(kolvo_raz))
rand=randint(0, rand_dapozon)
rand=str(abs(rand))
raz=len(rand)
podskazka = randint(0, raz-1)


print('У загаданного числа '+str(raz)+' '+check_raz(raz))
chislo = input('Введите ваш вариант: ')
i = 1
while chislo !=rand:
	print('Попытка №: '+str(i))	
	if chislo < rand:
		print('Не верно. Попробуйте выбрать число по-больше')
		if i % 5 == 0:
			if raz != 1:
				print('Подсказка: '+str(check_pod(podskazka))+' разряд числа это: '+str(rand[podskazka]))
	else:
		print('Не верно. Попробуйте выбрать число по-меньше')
		if i % 5 == 0:
			if raz != 1:
				print('Подсказка: '+str(check_pod(podskazka))+' разряд числа это: '+str(rand[podskazka]))
	chislo = input('Введите ваш вариант: ')
	i+=1
print('Вы угадали загаданное число это: '+str(rand))
	





