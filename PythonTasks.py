"""
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.
"""
number = int(input())
first, second, third, fourth = 0, 0, 0, 0

for _ in range(number):
    x, y = map(int, input().split())
    first += x > 0 and y > 0
    second += x < 0 and y > 0
    third += x < 0 and y < 0
    fourth += x > 0 and y < 0

print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")


"""
На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом. 

Формат входных данных
На вход программе подается строка текста из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести одно число – количество элементов списка, больших предыдущего.
"""
numbers = [int(n) for n in input().split()]
counter = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1
        
print(counter)


"""
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.

"""
a = [int(i) for i in input().split()]
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print (*a)



"""
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

Формат входных данных
На вход программе подается строка текста из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.

"""

a = [int(i) for i in input().split()]
a.insert(0, a[-1])
del a[-1]
print (*a)


"""
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

"""

a = [int(i) for i in input().split()]
print(len(set(a)))


"""
Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n\, (0 < n < 1000)n(0<n<1000) – количество чисел в наборе. В последующих nn строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может, другими словами, два множителя должны иметь разные индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы.

"""

l = [int(input()) for n in range(int(input()))]
n = int(input())
fl = False 

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] == n:
            fl = True
            break
            
print('ДА' if fl == True else 'НЕТ')






"""
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.

"""


a,b = str(input()),str(input())
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
     'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
     "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}
print(m[f"{a}-{b}"])



"""
Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.

Формат входных данных
На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.

"""

a,b = str(input()),str(input())
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}
print(m[f"{a}-{b}"])



"""
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 00.
"""

a = str(input()).split('О')
print(len(max(a)))



"""
Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".

"""

word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()




"""
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.

"""

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    for j in i:
        total += j
        counter += 1
print(total/counter)


"""
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно список, состоящий из nn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести построчно указанный список.

"""

n = int(input())
my_list = [[j for j in range(1, n + 1)] for i in range(1, n + 1)]
print(*my_list, sep='\n')


"""
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список, состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.

"""

n = int(input())
my_list = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
print(*my_list, sep='\n')


"""
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

Формат входных данных
На вход программе подается число n \, (n \ge 0)n (n≥0).

Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.

Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает соответствующую строку треугольника Паскаля.

Примечание 2. Графическая иллюстрация формирования треугольника Паскаля.

"""



n = int(input())
s = []
for i in range(n+1):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=i and j!=0: row[j] = s[i-1][j-1]+s[i-1][j]
    s.append(row)
print(s[n] if n!=0 else [1])


"""
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

"""

n = int(input())
P=[]
for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=P[i-1][j-1]+P[i-1][j]
    P.append(row)

for r in P:
    print(*r)



"""
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.
"""

res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)


"""
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.
"""

def chunked(st, n):
    st = st.split()
    a = [[] for _ in range(0, len(st), n)]
    for i in range(len(a)):
        a[i].extend(st[:n])
        st = st[n:]
    return a

string = input()
num = int(input())

print(chunked(string, num))


"""
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список в соответствии с примерами.

Примечание. Порядок списков одинаковой длины должен соответствовать порядку их вхождения в основной список.
"""

n=input().split()
o=[[]]
k=1
while k!=len(n)+1:
  for j in range(len(n)):
    if len(n[j:j+k])==k:
      o.append(n[j:j+k])
  k+=1
print (o)

"""
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице, далее идут n \times mn×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
"""

m, n, matrix = int(input()), int(input()), []
for i in range(m):
    matrix.append([input() for _ in range(n)])
    print(*matrix[i])


"""
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице, далее идут n \times mn×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу, но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.
"""

rows, cols = int(input()), int(input())
matrix = [[input() for _ in range(cols)] for i in range(rows)]
for i in matrix:
    print(*i)
print()
    
for i in range(cols):
    for x in range(rows):
        print( matrix[x][i], end=' ')
    print()


"""
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.


"""

n = int(input())
matrix = [[0]*n for i in range(n)]
for i in range(n):
    matrix[i] = input().split()

sum_first_diagonal = sum(int(matrix[i][i]) for i in range(n))
print(sum_first_diagonal)

"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести nn чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.
"""

n = int(input())
l = [input().split() for _ in range(n)]
counter = 0
for i in l:
    sr = (sum(list(map(int, i)))) / len(i)
    for j in i:
        if int(j) > sr:
            counter += 1
    print(counter)
    counter = 0


"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
"""

n = int(input())
arr = []
mtr = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i >= j:
            arr.append(mtr[i][j])
print(max(arr))

"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
"""


n = int(input())
s = []

for i in range(n):
    f = [int(i) for i in input().split()]
    for j in range(len(f)):
        if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
            s.append(f[j])

print(max(s))


"""
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте строковый метод ljust()).
"""

n, m = int(input()), int(input())

for i in range(n):
    for j in range(m):
        if j != m - 1:
            print(str((i * j)).ljust(2), end=' ')
        else:
            print(str((i * j)), end='')
    print()


"""
Напишите программу, которая поворачивает квадратную матрицу чисел на 90^{\circ}90 
∘
  по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
"""

n=int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for j in range(n):
    for i in range(n-1, -1, -1):
        print(matrix[i][j], end = ' ')
    print()


"""
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.
"""

x, y = [int(i) for i in input().split()]

matrix = [['.'] * y for _ in range(x)]

for i in range(x):
    if i == 0 or i % 2 == 0:
        for j in range(1, y, 2):
            matrix[i][j] = '*'
    else:
        for j in range(0, y, 2):
            matrix[i][j] = '*'

for row in matrix:
    print(*row)


"""
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:

числа на побочной диагонали равны 11;
числа, стоящие выше этой диагонали, равны 00;
числа, стоящие ниже этой диагонали, равны 22.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.
"""

n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    matrix[i][n-1-i] = 1
    for j in range(n):
        if i > n- 1- j:
            matrix[i][j] = 2
        print(matrix[i][j], end = " ")
    print()


"""
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.
"""

n = int(input())

matrix = []
for i in range(n):
    ii = n - i - 1
    row = [1 if i == j or ii == j else 0 for j in range(n)]
    matrix.append(row)
    
for row in matrix:
    print(*row)

"""
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.
"""
n = int(input())

for i in range(n):
    result =[]
    for j in range(n):
        if (i >= j and i >= n - 1 - j) or (i <= j and i <= n - 1 - j):
            result.append(1)
        else:
            result.append(0)
    print(*result)


"""
Напишите программу для вычисления суммы двух матриц.На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
"""
n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
a = input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix3[i][j] += matrix1[i][j] + matrix2[i][j]

for row in matrix3:
    print(*row)


"""
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

"""

l ,n,l1,c= input().split(),int(input()),[],0
for i in l:
   l1 += [l[c::n]]
   c += 1
   if c == n:
       break
print(l1)


"""
Транспонирование матрицы
Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка. 

"""

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
for i in zip(*matrix):
    print(*i)



"""
На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе подается нечетное натуральное число n, \, (n \ge 3)n,(n≥3) — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

"""

n = int(input())
a = [["."] * n for i in range(n)]
for i in range(n):
   a[i][i] = "*"
   a[n - 1 - i][i] = "*"
   a[i][n//2] = "*"
   a[n//2][i] = "*"
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))



"""
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

"""

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
        print('NO')
        break
else:
    print('YES')


"""
В переменную city_name вводится название города (например, Москва), а в переменную city_year – год его основания (например, 11471147). Заполните пропущенную строку таким образом, чтобы в переменной city оказался кортеж из значений этих двух переменных (сначала название города, затем год основания).

"""
city_name = input()
city_year = int(input())
city = tuple([city_name, city_year])
print(city)

"""
Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.

"""
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i != tuple()]

print(non_empty_tuples)



"""
Дополните приведенный код так, чтобы переменная new_tuples, содержала список кортежей на основе списка tuples с последним элементом каждого кортежа, замененным на численное значение 100100.

"""
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)

"""
Дополните приведенный код так, чтобы он вывел произведение элементов кортежа numbers.
"""
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
total = 1
for i in numbers:
    total = i*total
print(total)

"""
Программист Тимур написал программу для работы с биографическими данными русских поэтов. Данные содержатся в кортежах вида (фамилия, год рождения, город рождения). В процессе работы программы в некотором кортеже poet_data обнаружилась ошибка: ('Пушкин', 1799, 'Санкт-Петербург'), неверно указано место рождения, ведь Александр Пушкин родился в Москве.

Дополните приведенный код так, чтобы в переменной poet_data находился правильный кортеж (с исправленным значением), а затем выведите его содержимое.
"""

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
list_data = list(poet_data)
list_data[2] = 'Москва'
print(tuple(list_data))

"""
Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.
"""

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

l = []
for i in numbers:
  l.append(sum(i) / len(i))

print(l)

"""
Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.
"""
def coords(a, b, c):
    x = -(b / (2 * a))
    y = (4 * a * c - b**2) / (4 * a)
    return x, y

result = coords(int(input()), int(input()), int(input()))
print(result)

"""
Напишите программу, которая выводит список хорошистов и отличников в классе.

Формат входных данных
На вход программе подается натуральное число nn, далее следует nn строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

Примечание 1. Оценка ученика – это натуральное число от 11 до 55.

Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист – обладатель оценки 44, или отличник – получивший 55.
"""

lst = [input().split() for i in range(int(input()))]
    
for i in range(len(lst)):
    print(lst[i][0], lst[i][1])

print()

for i in range(len(lst)):
    if lst[i][1] in '45':
        print(lst[i][0], lst[i][1])



"""
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.

Формат входных данных
На вход программе подается одно число n\,  (n \le 100)n (n≤100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.
"""

def createTribonacci(limit, init=(2, 0, -1, 1)):
    a, b, c, d = init
    for _ in range(limit):
        a, b, c, d = b, c, d, 2*d - a
        yield d 
 
limit = int(input())
 
gen = createTribonacci(limit, init=(-3, 1, 1, -1))
print(*gen)


"""
На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. В результате nn учеников школы поехали отдыхать на море, mm учеников съездили в деревню, а kk учеников сходили в горы. Оказалось, что и в деревне, и на море были xx учеников, а в деревне и в горах — yy учеников. Побывать и в горах, и на море не удалось никому. 

Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу, а zz учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.

Формат входных данных
На вход программе подаются числа n, m, k, x, y, zn,m,k,x,y,z, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести одно число в соответствии с условием задачи.
"""

n, m, k, x, y, z = (int(input()) for _ in range(6))
print((n - x) + (m - x - y) + (k - y) + x + y + z)


"""
Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

«Что такое математика?»;
«Математическая составляющая»;
«100 гениальных идей по математике».

Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе, z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников. Всего в 10 классе учится aa учеников. Напишите программу, которая выводит сколько учеников:

прочитали только одну книгу;
прочитали две книги;
не прочитали ни одной из рекомендованных книг.
"""

n,m,k,x,y,z,t,a = [int(input()) for i in range(8)]
s1 = n + m - x - t
s2 = m + k - y - t
s3 = k + n - z - t
s = (n - s1 - s3 - t) + (m - s1 - s2 - t) + (k - s2 - s3 - t) # только одну книгу
print(s)  # только одну книгу
print(s1 + s2 + s3)  # только две книги
print(a - s - s1 - s2 - s3 -t )  # ничего не прочитали



"""
Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов множества numbers.
"""

numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}

print(max(numbers)+min(numbers))

"""
Дополните приведенный код, чтобы он вывел среднее арифметическое элементов множества numbers.
"""

numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers)/len(numbers)

print(average)

"""
Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.
"""
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
x = []
for i in numbers:
    x.append(i**2)
print (sum(set(x)))

"""
Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию (в обратном лексикографическом порядке).

Примечание. Выводите каждый элемент множества на отдельной строке.
"""

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits_sorted = sorted(fruits, reverse=True)
for i in fruits_sorted:
    print (i)


"""
На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?

Формат входных данных
На вход программе подается строка, состоящая из цифр

Формат выходных данных
Программа должна вывести YES если ни одна из цифр в строке не повторяется и NO в противном случае.
"""

string = str(input())
if len(string)==len(set(string)):
    print ('YES')
else:
    print ('NO')


"""
На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?

Формат входных данных
На вход подаются две строки, состоящие из цифр.

Формат выходных данных
Программа должна вывести YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.
"""

x, y = str(input()), str(input())
if len(set(x+y)) >= 10:
    print ('YES')
else:
    print ('NO')

"""
На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?

Формат входных данных
На вход подаются две строки, состоящие из цифр.

Формат выходных данных
Программа должна вывести YES, если для записи этих строк были использованы одинаковые наборы цифр и NO, в противном случае.
"""

x, y = set(input()), set(input())
if x==y:
    print ('YES')
else:
    print ('NO')




"""
На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

Формат входных данных
На вход программе подается строка, состоящая из трех слов.

Формат выходных данных
Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв и NO в противном случае.
"""

x, y, z = input().split(' ')
if set(x)==set(y) and set(y)==set(z):
    print('YES')
else:
    print('NO')
