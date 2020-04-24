from random import randint
import time

def get_gambling_field():
	cisla = [i for i in range(1,37)]
	list_chisel = [11,19,29]
	colors = ['Красный','Черный']
	twelve = {'Первая дюжина':[i for i in range(1,13)],'Вторая дюжина':[i for i in range(13,25)],'Третья дюжина':[i for i in range(25,37)]}
	row = {'Первый ряд':[i for i in range(1,35,3)],'Второй ряд':[i for i in range(2,36,3)],'Третий ряд':[i for i in range(3,37,3)]}
	color_list=[]
	i=1
	while i<37:
		if i in list_chisel:
			colors=list(reversed(colors))		
		for color in colors:
			color_list.append(color)
			i+=1	
	ready_dict={}
	for i in range(len(cisla)):
		ready_dict.update({cisla[i]:{'color':color_list[i]}})	
	for key,value in twelve.items():
		for chi in ready_dict:
			if chi in value:
				ready_dict[chi].update({'twelve':key})
	for key,value in row.items():
		for chi in ready_dict:
			if chi in value:
				ready_dict[chi].update({'row':key})			
	return ready_dict
print('Приветствуем Вас в игре рулетка. У нас есть 5 видов ставок.')
print('1 вид ставки: цвет Красный/Черный')
print('2 вид ставки: число от 1 до 36')
print('3 вид ставки: дюжины чисел (Первая дюжина - числа от 1 до 12, Вторая дюжина - от 13 до 24, Третья дюжина - от 25 до 36)')
print('4 вид ставки: ряды чисел (Певый ряд - числа от 1 до 34 с шагом 3, Второй ряд - от 2 до 35 с шагом 3, Третий ряд - от 3 до 36 с шагом 3)')
print('5 вид ставки: ставка на число 0')
print('\n')
stavka = input('Введите вашу ставку: ')
print('\n')
random_chislo = randint(0, 36)
for i in range(3):
	print('Шарик делает '+str(i+1)+' круг\n')
	time.sleep(1)	
pole = get_gambling_field()
if random_chislo == 0:
	print('Шарик упал на число 0')
else:	
	print('Шарик упал на '+str(random_chislo)+' '+pole[random_chislo]['color']+' цвет '+pole[random_chislo]['row']+' '+pole[random_chislo]['twelve']+'\n')
try: 
	int(stavka)
	if stavka == random_chislo:
		print('Позравляем ваша ставка на число '+stavka+'победила')
	else:
		print('К сожалению вы проиграли')	
except:
	param_stav=[]
	for key,value in pole[random_chislo].items():
		param_stav.append(value)
	if stavka not in param_stav:	
		print('К сожалению вы проиграли')			
	else:	
		print('Поздравляем ваша ставка на '+stavka+' победила')
			




