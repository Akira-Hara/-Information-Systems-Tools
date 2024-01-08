# Задача 1
string = input('Введите слово: ')
string = string.lower()
string_reversed = reversed(string)
if "yes" == "".join(set(["yes" if i == j else "no" for i, j in zip(string, string_reversed)])):
    print("Да")
else:
    print("нет")

# Задача 2
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end': #ключ стопер
        break
    m.append([int(s) for s in n.split()])
li = len(m)
new = [min(m[i]) for i in range(li)]
for i in range (li):
    print(new[i], end =' ')
    print()

# Задача 3
m = [] #список
d = {} #словарь
n = str(input())
m.append([str(s.lower()) for s in n.split()])
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j] #конкретное число в массиве
        if p in d:
            d[p]+=1 #выполняем поставленное условние
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)

# Задача 4
import pymysql

connect = pymysql.connect( #подключаемся к MySQL
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor() #описываем курсор
year= int(input('Введите год: ')) #вводим год
s = year
cur.execute(' select first_name,last_name,date_of_birth from user where year(date_of_birth) = %s',s)
for rec in cur: #вывод результата
    print(rec[0],rec[1],rec[2]) #rec0 = first name и тд.