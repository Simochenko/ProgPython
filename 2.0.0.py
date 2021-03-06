# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
'''
Напишите программу, которая считывает со стандартного
ввода целые числа, по одному числу в строке, и после
первого введенного нуля выводит сумму полученных на вход чисел.'''
# c = int (input())
# s = 0
# while c != 0:
#     s = s + c
#     c = int (input())
# print (s)

'''
Победителям соревнования достанется большой и вкусный пирог. 
В команде биологов a человек, а в команде информатиков — b человек. 

Нужно заранее разрезать пирог таким образом, чтобы можно было 
раздать кусочки пирога любой команде, выигравшей соревнование, 
при этом каждому участнику этой команды должно достаться одинаковое 
число кусочков пирога. И так как не хочется резать пирог на слишком 
мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных 
целых числа a и b, каждое число вводится на отдельной строке) и 
выводить наименьшее число d, которое делится на оба этих числа без остатка.
'''

# a = int (input())
# b = int (input())
# s = 1
# k = 2
# while s<k:
#   if s % a == 0 and s % b == 0:
#     k=s
#   else:
#     s=s+1
#     k=k+1
# print(s)
#
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

'''если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль.'''
#
# a = 0
# while a<=100:
#   a = int (input())
#   if a > 100:
#     break
#   if a<10:
#     continue
#   print(a)

'''Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа a, b, c и d, 
каждое в своей строке. Программа должна вывести фрагмент таблицы умножения 
для всех чисел отрезка [a;b] на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри 
строки используйте '\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся 
сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
'''
# a =int (input())
# b =int (input())
# c =int (input())
# d =int (input())
# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i*j),end='\t')
#     print(end='\n')

'''Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее 
арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12]. Всего чисел, 
делящихся на 3, на этом отрезке 6: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3'''

# a = int(input())
# b = int(input())
# s = 0
# c = 0
# for j in range (a,b+1):
#     if j%3 == 0:
#         s = s+j #42
#         c = c+1
#     j+=1
# print(s/c)

'''GC-состав является важной характеристикой геномных последовательностей и определяется как процентное 
"""GC-состав является важной характеристикой геномных последовательностей и определяется как процентное 
соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов G 
(гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и 
C равно 410⋅100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.'''

# a = input()  # input auto use type str
# s1 = a.upper().count('c'.upper())
# s2 = a.upper().count('g'.upper())
# S=s1+s2
# print(S/len(a)*100)


# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

'''Узнав, что ДНК не является случайной строкой, только что поступившие в Институте 
студенты группы информатиков предложили использовать алгоритм сжатия, 
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть 
группы одинаковых символов исходной строки заменяются на этот символ и 
количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её 
предложенным алгоритмом и выводит закодированную последовательность 
на стандартный вывод. Кодирование должно учитывать регистр символов.
'''

# s = str(input())
# l = len(s)-1
# c = 1
# t = ''
# if len(s)==1:
#     t = t +s+str(c)
# else:
#     for i in range(0,l):
#         if s[i]==s[i+1]:
#             c +=1
#         elif s[i]!=s[i+1]:
#             t = t + s[i]+str(c)
#             c = 1
#     for j in range(l,l+1):
#         if s[-1]==s[-2]:
#             t = t +s[j]+str(c)
#         elif s[-1]!=s[-2]:
#             t = t +s[j]+str(c)
#             c = 1
# print(t)

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(len(students))

# a = [1, 2, 3]
# b = a
# # значения списка b?
# print(*b, end=';')
# a[1] = 10
# # значения списка b?
# print(*b, end=';')
# b[0] = 20
# # значения списка a?
# print(*a, end=';')
# a = [5, 6]
# # значения списка b?
# print(*b)

'''Напишите программу, на вход которой подается одна строка с целыми числами. 
Программа должна вывести сумму этих чисел.

Используйте метод split строки. 
'''
# put your python code here
# s = [ int(i) for i in input().split()]
# summ = 0
# l = len(s)-1
# for i in range(0,l+1):
#     summ = summ + s[i]
# print(summ)

'''Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его 
соседей. Для элементов списка, являющихся крайними, одним из соседей 
считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход 
ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
#
# s = [ int(i) for i in input().split()]
# t = []
# l = len(s)-1
# k = 0
# i = 0
# if len(s)==0:
#     print(str(0))
# else:
#     for st in s:
#         if len(s)>1:
#             if i==0:
#                 k = s[i+1] + s[-1]
#                 t.append(k)
#             elif i>0 and i<l:
#                 k=s[i-1]+s[i+1]
#                 t.append(k)
#             elif i==l:
#                 k = s[i-1]+s[0]
#                 t.append(k)
#         elif len(s)==1:
#             k = s[i]
#             t.append(k)
#         i +=1
#     j = 0
#     for st2 in t:
#         print(str(t[j])+' ',end='')
#         j +=1

'''Напишите программу, которая принимает на вход список чисел 
в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода 
может быть произвольным'''

#
# s = [ int(i) for i in input().split()]
# t = []
# s.sort()
# l = len(s)-1
# k = 100000
# if len(s)!=1:
#     for i in range(0,l):
#         if s[i]==s[i+1] and s[i]!=k:
#             t.append(s[i])
#             k=s[i]
#     for j in range(l,l+1):
#         if s[-1]==s[-2] and s[j]!=k:
#             t.append(s[j])
# n = len(t)
# for g in range(0,n):
#     print(t[g],end=' ')

'''Напишите программу, которая считывает с консоли числа (по одному в строке) 
до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после 
этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется 
равной 0, после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент 
замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов, 
не обращая внимания на то, что остались ещё не прочитанные значения.'''

# a1 = int (input())
# s= a1
# s2 = 0+abs(a1**2)
# while s!=0:
#     a1 = int(input())
#     s = s + a1
#     s2 = s2+abs(a1)**2
#     if s==0:
#         break
# print(s2)

'''Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое 
число n — столько элементов последовательности должна отобразить программа. На выходе ожидается 
последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.'''

# p = []
# t = []
# M = []
# n = int(input())
# l = len(t)
# k = 0
# m = 2
# for h in range(1,n+1):
#     p.append(str(h))
# for i in range(0,len(p)):
#     if i==0:
#         t.insert(l,p[i])
#         k = 0
#     elif i==1:
#         while i>=k:
#             l = len(t)
#             t.insert(l,p[i])
#             k +=1
#         k -=2
#     elif i>1:
#         while i>=k:
#             l = len(t)
#             t.insert(l,p[i])
#             k +=1
#         k =i-m
#         m +=1
#     l = len(t)
# x = len(t)
# if len(t)==1:
#     print(1)
# else:
#     for j in range (0,x-1):
#         M.append(t[j])
#     for g in range(0,n):
#         print(M[g],end=' ')

'''Напишите программу, которая считывает список чисел lst из 
первой строки и число x из второй строки, которая выводит 
все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в 
списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию 
абсолютного значения.'''

# s = [ int(i) for i in input().split()]
# n = int(input())
# t = []
# l = len(s)-1
# if n in s:
#     for i in range(0,l+1):
#         if s[i]==n:
#             t.append(i)
#     g = len(t)-1
#     for j in range(0,g+1):
#         print(t[j],end=' ')
# else:
#     print('Отсутствует')


'''Напишите программу, на вход которой подаётся прямоугольная матрица 
в виде последовательности строк, заканчивающихся строкой, содержащей 
только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый 
элемент в позиции i, j равен сумме элементов первой матрицы на позициях 
(i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний 
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом 
по соответствующему направлению.'''

# n = ''
# m = []
# while True:
#     n = str(input()) # ввод строк
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])
# li, lj = len(m), len(m[0])
# new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
#
# for i in range (li):
#     for j in range (lj):
#         print(new[i][j], end =' ')
#     print()
'''Дополнительная
Выведите таблицу размером n \times n=n×n, заполненную числами от 11 до n^2n 
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):'''
#
#
# def spiral(n):
#     dx, dy = 1, 0
#     x, y = 0, 0
#     myarray = [[None] * n for j in range(n)]
#     for i in range(1, n ** 2 + 1):
#         myarray[x][y] = i
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
#             x, y = nx, ny
#         else:
#             dx, dy = -dy, dx
#             x, y = x + dx, y + dy
#     return myarray
#
#
# def printspiral(myarray):
#     n = range(len(myarray))
#     for y in n:
#         for x in n:
#             print(myarray[x][y], end=' ')
#         print()
#
#
# n = int(input())
# printspiral(spiral(n))


#
# def f(n):
#     return n * 10 + 5
#
#
# print(f(f(f(10))))
