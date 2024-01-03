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
# Public modules
import random
import os
import json
from datetime import date

# My modules
import crypto
import archive


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
    # print("... Data from JSON file #1:", data)

    # [+] Загрузить варианты логинов из файла с настройками (допустимо 4 шт.) и мастер пароль
    with open('secret_email_and_pas.json', encoding='utf-8') as fh:
        data_secret = json.load(fh)
    # print("... Data from JSON file #2:", data_secret)

    data.update(data_secret)  # Update data in dictionary

    # [+] Take the accounts saved in the zip-file and extract them to the working folder
    password_for_zip = data['master_password']
    archive.unzip_file(password_for_zip)
    with open('my_resources.txt', encoding='utf-8') as f:
        data_accounts = json.load(f)
        # print('... Accounts in resource file are:', data_accounts)

    # print('... ------------------------------------------- End of get_config()')

    return data, data_accounts


def user_input(data):
    """Take data from the user and save them."""

    def print_choice():  # Testing a nested function
        print('Your choice is:', str(login_choice) + ',', 'and login:', login)

    login = ''
    print('\nChoose login. Type the number:\n'
          '[1] Mail.ru\n'
          '[2] Gmail.com\n'
          '[3] Цифра\n'
          '[4] Cell phone\n'
          '[5] Input manually')
    login_choice = int(input())

    # [+] Take resource from JSON
    if login_choice == 1:
        login = data['mail.ru']
        print_choice()
    elif login_choice == 2:
        login = data['gmail.com']
        print_choice()
    elif login_choice == 3:
        login = data['zyfra.com']
        print_choice()
    elif login_choice == 4:
        login = data['cellphone']
        print_choice()
    elif login_choice == 5:
        login = input('Input login: \n')
        print_choice()
    else:
        print('There is no such choice. Try again.')
        main()

    resource = str(input('Type or paste the name of the resource for which '
                         'a password is required: \n'))
    password_length = int(input('Enter password length: \n'))
    # print('... ------------------------------------------- End of user_input()')

    return login, resource, password_length


# def encrypt(master_password, second_password, data):
#     """Encrypts data with second and master password"""
def encrypt(text, shift):
    """Software implementation of the Caesar encryption algorithm"""
    # Maybe later - Зашифровать для хранения, пропустив через шифр Цезаря (look code below);
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
    """Generate password and return a list of passwords and their number"""
    # Not now. Ввод пароля в русском алфавите с сохранением, например "Дом1", чтобы перевело в "Ljv1"
    # Not now. Хранить значения: русское написание, англ. написание, сам пароль, ресурс
    # [+] Генерация пароля c выбором доступного набора символов (сайты могут не разрешать символы)
    # [+] Add the password creation date to the array (list)

    length = password_length
    single_password = ''
    chars = ''
    chars_w_signs = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    chars_wo_signs = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    print('Choose chars to use:\n',
          '[1] This dictionary with signs :', chars_w_signs, '\n',
          '[2] Or dictionary without signs:', chars_wo_signs, '\n')
    chars_choice = int(input())
    print('Chars_choice', chars_choice)
    if chars_choice == 1:
        chars = chars_w_signs
    elif chars_choice == 2:
        chars = chars_wo_signs

    # Way 1. Single password (Store it)
    for _ in range(length):
        single_password += random.choice(list(chars))  # Chars for random
    print(f'Your single password for resource: "{resource}" , login: "{login}", '
          f'with length "{length}" is: {single_password}\n')

    date_today = str(date.today().strftime('%Y.%m.%d'))
    account = [resource, login, single_password, length, date_today]  # Save in massive (list)
    # accounts = [account]
    # print('... Account:', account, 'Accounts:', accounts)

    # Way 2. Multiple passwords (Do not store, just for fun)
    passwords_list = []
    # print('... ------------------------------------------- generate(), Start Way 2')
    number = int(input('Generate other passwords of the same length?\n'
                       'Please, enter the number of passwords\n'
                       'Type [0] to exit the program\n'
                       'Type [1] to continue with the single password'))
    if number == 0:  # I did not return to re-enter the value because this condition for fun
        print('You have entered "0" passwords. Exit the program')
        raise SystemExit
    if number == 1:
        pass
    if number != 1:
        for _ in range(number):  # To avoid unused variable warning in Pylint, replaced by (‘_’).
            password = ''
            for _ in range(length):
                password += random.choice(chars)
                # Инструкция i += 1 эквивалентна конструкции i = i + 1 (это просто сокращенная запись)
                # Оператор += комбинированный оператор присваивания и сложения. Он увеличивает
                # значение переменной на указанное число (в данном случае на 1)
                # и присваивает полученное значение обратно переменной.
            # print(password)
            passwords_list.append(password)

            for item in passwords_list:
                print(item)

    return account


def output(accounts, data):
    """Final information about the program"""
    print(f'\nConfiguration from JSON: {data}\n')
    print(f'Your accounts: {accounts}\n')

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
    # d = dict(izip(names, colors))


def save_file(file_name_txt, accounts):
    """Save file with accounts"""

    # my_resources.txt
    with open(file_name_txt, 'w', encoding='utf-8') as f:
        json.dump(accounts, f, ensure_ascii=False, indent=4)
    print('... File', file_name_txt, 'saved!')
    # print('... ------------------------------------------- End of save_file()')


def find_and_show():
    """Find and print all accounts from archive"""
    # TODO. Вытащить из архива, расшифровать найти и отобразить - No need. I can do it in text file
    # TODO. Show all available accounts

    # crypto.encrypt_decrypt(encrypted_text, decrypt_flag, shift)
    print('Accounts:\n')


def main():
    """I can quickly comment out the function call from here"""

    data, data_accounts = get_config()
    login, resource, password_length = user_input(data)
    # print('\n... All options from JSON:\n', data)
    # print('\n... Data_accounts in archive:\n', data_accounts)
    account = generate(resource, login, password_length)
    accounts = [account] + data_accounts
    print('\nAdded to archive:', account)
    output(accounts, data)
    file_name_txt = data['file_name_txt']
    save_file(file_name_txt, accounts)
    # Zip and unzip accounts
    password_for_zip = data['master_password']
    archive.zip_file(password_for_zip)

    print()
    exit_or_fun = int(input('[0] Exit\n[1] Fun with encryption\n'))
    if exit_or_fun == 0:  # I did not return to re-enter the value because this condition for fun
        print('You have entered "0". Exit the program')
        raise SystemExit
    if exit_or_fun == 1:
        print('...Continue')
    else:
        print('...Continue')

    # Encrypt text test
    # Not now. Spaces and decrypt
    text = str(input('Enter the text to encrypt the password (no spaces please): ' + "\n"))
    # text = 'ABCD'   # After encrypt should be 'E F G H'
    shift = 4
    result_encrypt = encrypt(text, shift)  # Function returns 1 value - text
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
    # Not now. Test result: DromTestFindGen - > D T F G after Hack
    # result_decrypt = hack_cipher(encrypted_text)
    # print('result_decrypt, last value', result_decrypt)

    # Module two
    print('... ------------------------------------------- main() -> crypto.py')
    decrypt_flag = 2
    crypto.encrypt_decrypt(encrypted_text, decrypt_flag, shift)
    # Not now. Test result: DromTestFindGen -> DROMTESTFINDGEN (all capitals after decrypt!)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
