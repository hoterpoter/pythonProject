import pandas as pd
df = pd.read_csv('C:/Users/Hoterpoter/PycharmProjects/pythonProject/sample_data/california_housing_train.csv')
# print(df.head(5)) #функция, которая показывает первые 5 строк таблицы
# print(df.tail(5)) # функция, которая показывает последние 5 строк таблицы
# print(df.shape)  #Функция shape возвращает размеры таблицы: кортеж из 2 значений, 1 - количество строк, 2 - количество столбцов
# print(df.isnull()) # Чтобы обнаружить пустые значения в таблице данных необходимо воспользоваться функцией .isnull()
# print(df.isnull().sum()) #функцией .sum(). Данная функция выведет количество null-значений в каждой ячейке по столбцам
# print(df.dtypes)# у каждого столбца есть свой тип данных, чтобы это узнать, нужно применить функцию .dtypes
# print(df.columns) # узнать название всех столбцов в таблице, воспользуйтесь функцией.columns.
# print(df[['latitude', 'population']])
# print(df[df['housing_median_age'] < 20])
# print(df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]) #проверять несколько условий сразу.
#
print(df['population'].max())# Максимальное значение
print(df['population'].min())#Минимальное значение:
print(df['population'].mean())#Среднее значение
print(df['population'].sum()) #Сумма:
print(df.describe()) ''' Перцентиль - это показатель, используемый в статистике,
показывающий значение, ниже которого падает определенный процент
наблюдений в группе наблюдени 
'''


