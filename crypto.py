"""Software implementation of the Caesar encryption algorithm"""


def encrypt_decrypt(text, decrypt_flag, shift):
    """Encrypt and decrypts text, if decrypt_sign is 2 - decrypt, other - encrypt"""
    print('The text came into the function:', text)
    en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if decrypt_flag == 2:
        shift = -shift  # For Decrypt, test
    else:
        shift = int(input('Encryption step (shift). For example 4 for encrypt, -4 for decrypt: '))
    # message = input("Message to encrypt or decrypt (only letters): ").upper()

    # There are some troubels with spaces
    # For this ""CEASER CIPHER DEMONSTRATION" we get "CEASERNCIPHERNDEMONSTRATION"
    # message = 'GIEWIVrGMTLIVrHIQSRWXVEXMSR'.upper()
    message = text.upper()      # Upper case is used to avoid errors
    result = ''
    lang = input('Choose language. Type "1" for Russian, "2" for English: ')
    if lang == '1':
        for i in message:
            place = ru_alphabet.find(i)
            new_place = place + shift
            if i in ru_alphabet:
                result += ru_alphabet[new_place]
            else:
                result += i
    else:
        for i in message:
            place = en_alphabet.find(i)
            new_place = place + shift
            if i in en_alphabet:
                result += en_alphabet[new_place]
            else:
                result += i
    print('Result:', result)
