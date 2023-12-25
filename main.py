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
#     encrypt(string, int) -> string
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
import crypto


def get_config():
    """Import JSON, define variables."""
    # Method search for user’s home directory in password directory
    # On Windows platform, an initial ~ is replaced by the value of HOME and USERPROFILE
    # Функция expanduser() модуля os.path возвращает аргумент с начальным компонентом
    # пути '~' или '~user', замененным домашним каталогом этого пользователя.
    directory = os.path.expanduser("~/.password.zip")

    # Load from JSON
    with open('settings.json', encoding='utf-8') as fh:  # Open the file for reading
        data = json.load(fh)  # Load data from the file into the data dictionary
    data['Path'] = '"' + directory + '"'
    print("... Data from JSON file:", data)

    # master_password = ''

    # # Extracting zip with password
    # file_name = 'password.zip'
    # second_password = 'data'

    # with zipfile.ZipFile(file_name) as file:
    #     # Password must be in the bytes converted 'str' into 'bytes'
    #     # 'setpassword' method is used to give a password to the 'Zip'
    #     file.setpassword(pwd=bytes(second_password, 'utf-8'))
    #     file.extractall()
    print('... ------------------------------------------- End of get_config()')

    return data


def user_input():
    """Take data from the user and save them."""
    def print_choice():     # Testing a nested function
        print('Your choice is:', login_choice, 'Login:', login)

    login = ''
    login_choice = int(input('\nType your choose. My logins: 1. Mail.ru 2. Gmail.com 3. Цифра, '
                             '4. Cell phone, 5. Input manually \n'))
    if login_choice == 1:
        login = 'vas_ky@mail.ru'
        print_choice()
    elif login_choice == 2:
        login = 'klino_vitsky@gmail.com'
        print_choice()
    elif login_choice == 3:
        login = 'vladi_mir.klinovickiy@zyfra.com'
        print_choice()
    elif login_choice == 4:
        login = '123321_89059077777'
        print_choice()
    elif login_choice == 5:
        login = input('Input login: \n')
        print_choice()
    else:
        print('There is no such choice. Try again.')
        main()
    # TODO. Save user_login to dict

    resource = str(input('Type or paste the name of the resource for which '
                         'a password is required: \n'))
    # TODO. Get and save recourse, For example "google.com"

    password_length = int(input('Enter password length: \n'))

    # TODO. Temporary return variables from function (see return)
    print('... ------------------------------------------- End of user_input()')

    return login, resource, password_length


# def encrypt(master_password, second_password, data):
#     """Encrypts data with second and master password"""
def encrypt(text, shift):
    """Software implementation of the Caesar encryption algorithm"""
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def hack_cipher(text):
    """Find the key in a strange way (Hack algorithm?)"""
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assumptions = {}
    # Attempt to hack the cipher
    for key in range(len(letters)):
        translated = ''
        for symbol in text:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                    translated = translated + letters[num]
                else:
                    translated = translated + symbol
        assumptions[key] = translated
        print('Decrypt key #%s: %s' % (key, translated))

    return assumptions[30]  # Take the key with the right answer (always key # 30)


def generate(resource, login, password_length):
    """Generate passwords and return a list of passwords and their number"""

    length = password_length
    single_password = ''
    passwords_list = []
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    # Way 1. Single password
    for _ in range(length):
        single_password += random.choice(list(chars))  # Chars for random
    print(f'Your single password for resource: "{resource}" , login: "{login}", '
          f'with length "{length}" is: {single_password}')

    # Way 2. Multiple passwords
    print('... ------------------------------------------- generate(), Start Way 2')
    number = int(input('Generate other passwords of the same length?\n'
                       'Please, enter the number of passwords (or type "0" to exit): ' + "\n"))
    if number == 0:     # I did not return to re-enter the value because this condition for fun
        print('You have entered "0" passwords. Exit the program')
        raise SystemExit

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


def output(passwords_list, number, options):
    """Final information about the program"""
    print(f'... Configuration from JSON in output(): {options}')
    print(f'Your {number} password(s): {passwords_list}')

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
    login, resource, password_length = user_input()
    options = get_config()
    passwords_list, number = generate(resource, login, password_length)
    output(passwords_list, number, options)

    print('... ------------------------------------------- main()')
    # Encrypt text test
    # TODO. Spaces and decrypt
    text = str(input('Enter the text to encrypt the password (no spaces please): ' + "\n"))
    # text = 'ABCD'   # After encrypt should be 'EFGH'
    shift = 4
    result_encrypt = encrypt(text, shift)   # Function returns 1 value - text
    print("Plain Text : " + text)
    print("Shift pattern : " + str(shift))
    print("Cipher result: ", result_encrypt)

    # result_test = encrypt('CEASER CIPHER DEMONSTRATION', 4)
    # print('Cipher for string "CEASER CIPHER DEMONSTRATION" with shift "4" is:', result_test)

    # Decrypt encrypted text
    # encrypted_text = 'EFGH'
    encrypted_text = result_encrypt
    result_decrypt = hack_cipher(encrypted_text)
    print('Hack complete. The key number #30 is:', result_decrypt)
    # TODO. Test result: DromTestFindGen - > DTFG after Hack
    # result_decrypt = hack_cipher(encrypted_text)
    # print('result_decrypt, last value', result_decrypt)

    #Module two
    print('... ------------------------------------------- main() -> crypto.py')
    decrypt_flag = 2
    crypto.encrypt_decrypt(encrypted_text, decrypt_flag, shift)
    # TODO. Test result: DromTestFindGen -> DROMTESTFINDGEN (all capitals after decrypt!)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
