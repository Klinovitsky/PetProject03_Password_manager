"""Pet-project 03. Password manager"""
# ----------------------------------------------------------------------------------------------
# ТЗ: Менеджер паролей с шифрованием и генератором паролей
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# (c) 2023 Vladimir Klinovitsky, Moscow, Russian Federation
# e-mail: klinovitsky@gmail.com
#
# Functions:
#     get_config(file) - > object
#     settings(object, file) -> list
#     generate(object) -> object
# Misc variables:
#     master_password
# ----------------------------------------------------------------------------------------------

import random
import os
import json
import getpass
import datetime
import zipfile


def get_config():
    """Import JSON, define variables."""
    # Method search for user’s home directory in password directory
    # On Windows platform, an initial ~ is replaced by the value of HOME and USERPROFILE
    config = os.path.expanduser("~/.password.zip")

    # master_password = ''

    # # Extracting zip with password
    # file_name = 'password.zip'
    # second_password = 'data'

    # with zipfile.ZipFile(file_name) as file:
    #     # Password must be in the bytes converted 'str' into 'bytes'
    #     # 'setpassword' method is used to give a password to the 'Zip'
    #     file.setpassword(pwd=bytes(second_password, 'utf-8'))
    #     file.extractall()

    return config


def add():
    """Calculate the sum."""


def encrypt(master_password, second_password, data):
    """Encrypts data with second and master password"""


def decrypt(master_password, second_password, data):
    """Decrypts data with second and master password"""


def generate():
    """Generate passwords and return a list of passwords and their number"""
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = int(input('Enter the number of passwords: '))

    if number == 0:     # I did not return to re-enter the value because this condition for fun
        print('You have entered 0 passwords. Exit the program')
        raise SystemExit

    length = int(input('Enter password length: '))
    passwords_list = []

    for _ in range(number):     # To avoid unused variable warning in Pylint, replaced by (‘_’).
        password = ''
        for _ in range(length):
            password += random.choice(chars)

            # Оператор += является комбинированным оператором присваивания и сложения.
            # Он увеличивает значение переменной на указанное число (в данном случае на 1)
            # и присваивает полученное значение обратно переменной.
            # Инструкция i += 1 эквивалентна конструкции i = i + 1 (это просто сокращенная запись)
        # print(password)
        passwords_list.append(password)
    return passwords_list, number


def output(passwords_list, number, config):
    """Final information about the program"""
    print(f'Configuration: {config}')
    print(f'The number of passwords generated: {number}')
    print(f'Password(s): {passwords_list}')


    # Workpiece 1.
    # colors = ['red', 'green', 'blue', 'yellow']
    #
    # for color in colors:
    #     print(color)

    # Workpiece 2. Заготовка для подсчета элементов в словаре, описание работы см. ниже:
    # https://docs.python.org/dev/library/collections.html#collections.defaultdict
    # d = defaultdict(int)
    # for word in words:
    #     d[word] += 1

    # Workpiece 3.
    # Соединение 2 списков в 1 словарь.
    # Очень быстрый метод, используется только один кортеж для генерации словаря.
    # names = ['raymond', 'rachel', 'matthew']
    # colors = ['red', 'green', 'blue']
    #
    # d = dict(izip(names, colors))


def main():
    """I can quickly comment out the function call from here"""
    config = get_config()
    settings()
    add()
    passwords_list, number = generate()
    output(passwords_list, number, config)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
