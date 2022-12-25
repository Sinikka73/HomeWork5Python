"""
 Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
 выводить ее на экран.
"""

try:
    with open('task5.txt', 'w', encoding='utf-8') as file:
        data = input('Введите цифры через пробел: ')
        file.writelines(data)
        my_lst = data.split()
        print(f"Сумма чисел: {sum(map(int, my_lst))}")
except ValueError:
    print('вводите только числа')