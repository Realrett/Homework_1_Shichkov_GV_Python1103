# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

a = int(input('Введите положительное число: '))
if a <= 0:
    a = int(input('Введите положительное число: '))
b = str(a) + str(a)
c = str(a) + str(b)
d = a + int(b) + int(c)
print(a,'+',b,'+',c,'=', d)