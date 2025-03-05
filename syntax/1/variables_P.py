"""
Этот файл содержит 5 заданий по переменным и типам данных в Python
с их решениями и объяснениями для начинающих.
"""

# 1. Преобразование типов и работа со строками
"""
Тема: В Python можно преобразовывать одни типы данных в другие.
Например, число можно превратить в строку, а строку обратно в число.

Задание: Программа запрашивает у пользователя два числа,
преобразует их в int, складывает и выводит результат.
"""
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

num1 = int(num1)  # Преобразуем в число
num2 = int(num2)  # Преобразуем в число

result = num1 + num2  # Складываем числа

print("Сумма чисел:", result)
print()

# 2. Работа со списками: добавление и удаление элементов
"""
Тема: Списки позволяют хранить несколько значений в одной переменной.
Можно добавлять, удалять элементы и получать доступ по индексу.

Задание: Программа создает список из 3 слов, добавляет к нему еще одно,
затем удаляет первое слово и выводит итоговый список.
"""
words = ["яблоко", "банан", "вишня"]
words.append("груша")  # Добавляем новый элемент
words.pop(0)  # Удаляем первый элемент списка

print("Обновленный список слов:", words)
print()

# 3. Словари: работа с ключами и значениями
"""
Тема: Словари хранят данные в формате "ключ: значение".
Позволяют быстро находить значения по ключу.

Задание: Программа создает словарь с оценками студентов.
Добавляет новую запись и изменяет оценку существующего студента.
"""
students = {"Анна": 5, "Иван": 4, "Мария": 3}
students["Петр"] = 5  # Добавляем нового студента
students["Мария"] = 4  # Изменяем оценку

print("Список студентов и их оценок:", students)
print()

# 4. Проверка типа данных
"""
Тема: В Python есть функция type(), которая позволяет узнать тип данных переменной.

Задание: Программа запрашивает у пользователя ввод, затем определяет и выводит его тип данных.
"""
user_input = input("Введите что-нибудь: ")
print("Тип введенных данных:", type(user_input))
print()

# 5. Работа с кортежами: безопасное извлечение элемента
"""
Тема: Кортежи (tuple) — это неизменяемые списки. Изменять их нельзя, но можно получать значения по индексу.

Задание: Программа создает кортеж и позволяет пользователю безопасно получить элемент по индексу.
"""
tuple_example = (10, 20, 30, 40, 50)
index = int(input("Введите индекс элемента (0-4): "))

print("Элемент кортежа:", tuple_example[index])
