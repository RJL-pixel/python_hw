# # 1
#
# st = 'as 23 fdfdg544'
# print(','.join([g for g in st if g.isdigit()]))
#
#
# #2
#
# st = 'as 23 fdfdg544 34'
#
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))
#
# #list comprehension
#
#
#
# #1
#
# greeting = 'Hello, world'
# print([ch.upper() for ch in greeting])
#
# #2
#
# print([i**2 for i in range(50) if i % 2])
#
# #function
#
#
#
# #- створити функцію яка виводить ліст
#
#
# def show(ls):
#     print(ls)
#
# #- створити функцію яка приймає три числа та виводить та повертає найбільше.
#
# def max(a, b, c ):
#     max1 = max(a, b, c)
#     print(max1)
#     return max1
#
# #- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
#
# def min_max(*args):
#     print(max(args))
#     return min(args)
#
# #- створити функцію яка повертає найбільше число з ліста
#
# def max_of_list(ls):
#     return max(ls)
# #- створити функцію яка повертає найменьше число з ліста
#
# def min_of_list(ls):
#     return min(ls)
#
# #-створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
# def sum_of_list(ls):
#    sum(ls)
#
# #- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# # def avg(ls):
# #     return sum(ls)/ len(ls)
#
#
#
#
# #  - знайти мін число
def find_min():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(min(ls))

#  - видалити усі дублікати
def set_from_list():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(list(set(ls)))
#    - замінити кожне 4-те значення на 'X'
def swap_to_x():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(['X' if not (i+1)%4 else v for i,v in enumerate(ls)])



# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
         if i==0 or i==n-1:
                print('*'*n)
         else:
             print('*'+ ' '*(n-2)+'*')





def multi_table():
    i = 1
    while i<=9:
        j =1
        while j<=9:
            res = i*j
            print(f'{res:4}',end='')
            j+=1
        i+=1
        print()






while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) змінити кожне 4-те значення на Х')
    print('4) вивести на екран пустий квадрат з "*" ')
    print('5) вывести табличку множення за допомогою цикла while ')
    print('9) вихід ')
    choise = input('Зробіть ваш вибір: ')

    if choise == '1':
        find_min()
    elif choise =='2':
        set_from_list()
    elif choise =='3':
        swap_to_x()
    elif choise == '4':
        square(6)
    elif choise == '5':
        multi_table()
    elif choise == '9':
        break
    print('\n')


