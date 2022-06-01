import string

def caesar_cipher(string, shift_amount):
    dictionary = dict.fromkeys(string.ascii_lowercase, 0)

    for char in dictionary:
        print(char)

caesar_cipher("Boy! What a string!", -5)