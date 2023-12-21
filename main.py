# ----------------------------------------------------------------------------------------------
# Pet-project 03. Password manager
#
# ТЗ: Менеджер паролей с шифрованием и генератором паролей
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# (c) 2023 Vladimir Klinovitsky, Moscow, Russian Federation
# e-mail: klinovitsky@gmail.com
# ----------------------------------------------------------------------------------------------

import random
import os
import json
import getpass
import datetime
import zipfile


def get_config():
    # Method search for user’s home directory in password directory
    # On Windows platform, an initial ~ is replaced by the value of HOME and USERPROFILE
    config = os.path.expanduser("~/.password.zip")

    master_password = ''

    # # Extracting zip with password
    # file_name = 'password.zip'
    # second_password = 'data'

    # with zipfile.ZipFile(file_name) as file:
    #     # Password must be in the bytes converted 'str' into 'bytes'
    #     # 'setpassword' method is used to give a password to the 'Zip'
    #     file.setpassword(pwd=bytes(second_password, 'utf-8'))
    #     file.extractall()

    return config


def settings():
    """Import JSON, define variables."""
    pass


def add():
    """Calculate the sum."""
    pass


def encrypt(master_password, second_password, data):
    """Encrypts data with second and master password"""


def decrypt(master_password, second_password, data):
    """Decrypts data with second and master password"""


def generate():
    """Generate password."""

    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = input('Enter the number of passwords: ')
    length = input('Enter password length: ')
    number = int(number)
    length = int(length)

    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)

        print(password)


def output(items):
    """Final information about the program"""
    print(f'Password(s) generated: {items}')

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
    # Соединение 2 списков в 1 словарь. Очень быстрый метод, используется только один кортеж для генерации словаря.
    # names = ['raymond', 'rachel', 'matthew']
    # colors = ['red', 'green', 'blue']
    #
    # d = dict(izip(names, colors))


def main():
    get_config()
    settings()
    add()
    generate()
    output('report_file.zip')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
