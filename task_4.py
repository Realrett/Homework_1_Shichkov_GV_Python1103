# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника

revenue = int(input('Введите показатель выручки: '))
costs = int(input('Введите показатель издержек: '))
staff = int(input('Введите количество сотрудников: '))
profit = revenue - costs
profitability = round(profit / revenue * 100 , 2)
PPP = profit / staff
if profit > 0:
    print('Получена прибыль в размере', profit, 'денежных единиц')
    print('Рентабельность положительная и составляет', profitability, 'процентов')
    print('Прибыль на единицу персонала составляет:', PPP, 'денежных единиц')
elif profit < 0: 
    print('Получен убыток в размере', profit, 'денежных единиц')
    print('Рентабельность отрицательная и составляет', profitability, 'процентов')
    print('Убыток на единицу персонала составляет:', PPP, 'денежных единиц')
else: print('Получена нулевая прибыль. Показатели рентабельности и прибыли на единицу персонала также нулеввые.')
    
    
    