#Задание 2
    print ("Hello world") #Команда print выводит сообщения

#Задание 3
    a = 3
    print(type(a)) #int – целочисленный тип
    a = 3.5
    print(type(a)) #float – вещественный
    a = 'qwerty'
    print(type(a)) #str – строчный
    a = True
    print(type(a)) #bool – логический
    a = '123'
    print(type(a)) #str – строчный
#Мы не можем складывать строчный и целочисленный тип

#Задание 4
    a = 5.7
    print(int(a)) #первая задача
    a = -5.7
    print(int(a)) #вторая задача
    a = 3**39 - int(float(3**39))
    print(a) #третья задача (Ответ:11)

#Задание 5
    a = input('Как ваше имя? ') #Инпут запоминает значение
    print('Будем знакомы,',a,'!')

#Задание 6
    x = int(input('Количество часов до частной клиники: '))
    y = int(input('Количество минут до поликлиники: '))
    m = sum(x * 60 + y for m in range(2)) #Выражение - генератор
    print ('Итого минут: ',m)

#Задача 7
    a = False
    b = True
    c = False
    print (not a or b and c) #задание 1 (выходит True)
    print (not (a or b) and c) #задание 2 (выходит False)

#Задача 8
a = int(input('Введите год рождения: '))
if a < 1900 or a > 3000:  # Выборка в указанном периоде
    print('Год не подходит в выборку.')
elif a % 4 == 0 and a % 400 != 0:  # Остаток от деления на 4 для выяснения четности
    print('С днём рождения!:)')
else:
    print('Год обычный :(')

#Задача 9
    a = 1
    while a <= 20:
        if a % 2 == 0:  # Остаток от деления на 2
            print(a, end=' ')  # Ставим в конец через пробел
        a += 1

#Задача 10
    a=1
    b=0
    while a !=0: #цикл, пока а не равно нулю
        a = int(input('Введите число: '))
        b=b+a
    print(b)

#Задача 11
    x = int(input('Количество коллег в клинике: '))
    y = int(input('Количество коллег в поликлинике: '))
    a = 2
    while a % y != 0 or a % x != 0:  # Цикл для нахождения НОК
        a += 1
    print('Нужно кусков: ',a)

#Задача 12
    a=0
    for a in range(1,20+1): #цикл for
        if a%2 == 0: #проверка на четность
            print(a, end=' ')
    a +=1

#Задача 13
    a = int(input('Введите значение: '))
    b = int(input('Введите значение: '))
    c = int(input('Введите значение: '))
    d = int(input('Введите значение: '))
    print('', end='\t')  # Первый отступ, пустой
    for j in range(c, d + 1):  # Первый ряд чисел
        print(j, end='\t')
    print()  # Переход на следующий ряд
    for i in range(a, b + 1):  # Для данного ряда чисел
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')  # Умножаем 2 числа
        print('\t')
    print()

#Задача 14
    n = int(input('Введите значение матрицы: '))
    a = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):   # заполнение 1 строки
        count += 1
        a[0][i] = count
    j = 0
    i = n-1
    n -= 1  # устанавливаем размер 1 блока 1 витка
    while len(a)**2 != count:  #условие выхода из цикла
        for k in range(n):  #движение вниз
            j += 1
            count += 1
            a[j][i] = count
        for k in range(n):  #движение влево
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1):  #движение вверх
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1): #движение вправо
            i += 1
            count += 1
            a[j][i] = count
        n -= 2    # обеспечиваем переход на внутренний виток
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#Задача 15
    import time
    from tkinter import messagebox

    while True: #Цикл для бесконечности
        time.sleep(10) #Каждые 10 секунд
        if __name__ == '__main__':
            messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')