import pandas as pd
import numpy as np
import datetime
data_csv = pd.read_csv('avocado.csv')
# удаляем TotalUS из отбора
df_new = data_csv.drop(np.where(data_csv['region'] == 'TotalUS')[0])
# получаем максимальное значение AveragePrice
max_AveragePrice = df_new[df_new.AveragePrice == df_new.AveragePrice.max()]
#Подсчет суммы проданных авакадо для каждого дня
max_data_4046 = df_new.groupby(by = ['Date'],as_index=False)['4046'].sum()
max_data_4225 = df_new.groupby(by = ['Date'],as_index=False)['4225'].sum()
max_data_4770 = df_new.groupby(by = ['Date'],as_index=False)['4770'].sum()

#Подсчет максимального значения для каждого вида авакадо
max_PLU_4046 = max_data_4046[max_data_4046['4046'] == max_data_4046['4046'].max()]
max_PLU_4225 = max_data_4225[max_data_4225['4225'] == max_data_4225['4225'].max()]
max_PLU_4770 = max_data_4770[max_data_4770['4770'] == max_data_4770['4770'].max()]

#Получение даты максимальной продажи

date_max_AveragePrice = datetime.datetime.strptime(max_AveragePrice.Date.values[0],'%Y-%m-%d').strftime('%d.%m.%Y')
date_max_PLU_4046 = datetime.datetime.strptime(max_PLU_4046.Date.values[0],'%Y-%m-%d').strftime('%d.%m.%Y')
date_max_PLU_4225 = datetime.datetime.strptime(max_PLU_4225.Date.values[0],'%Y-%m-%d').strftime('%d.%m.%Y')
date_max_PLU_4770 = datetime.datetime.strptime(max_PLU_4770.Date.values[0],'%Y-%m-%d').strftime('%d.%m.%Y')

print('Самая большая средняя цена на авакадо была '+str(date_max_AveragePrice)+' в регионе '+str(max_AveragePrice.region.values[0]))
print('PLU_4046 был наиболее популярен '+str(date_max_PLU_4046))
print('PLU_4225 был наиболее популярен '+str(date_max_PLU_4225))
print('PLU_4770 был наиболее популярен '+str(date_max_PLU_4770))


