import pandas as pd

data_excel = pd.read_excel('Data.xlsx')
print(data_excel)
print('Сумма значений массива "Сумма" '+str(data_excel['Сумма'].sum()))
print('Среднее арифметическое значений массива "Сумма" '+str(data_excel['Сумма'].mean()))
print('Среднеквадратичное отклонение значений массива "Сумма" '+str(data_excel['Сумма'].std()))