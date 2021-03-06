number_of_lowercase_letters = 26


def new_char(char, shift):
    """make new char using value of shift"""
    ord_char = ord(char)
    if (ord_char - ord('A') >= 0) and (ord('Z') - ord_char >= 0):
        new_ord = (ord_char - ord('A') + shift) % number_of_lowercase_letters + ord('A')
        return chr(new_ord)
    elif (ord_char - ord('a') >= 0) and (ord('z') - ord_char >= 0):
        new_ord = (ord_char - ord('a') + shift) % number_of_lowercase_letters + ord('a')
        return chr(new_ord)
    else:
        return char


def caesar_encode_string(main_string, shift):
    """"encode caesar string"""
    new_string = []
    for char in main_string:
        new_string.append(new_char(char, shift))
    return ''.join(new_string)


def caesar_decode_string(main_string, shift):
    return caesar_encode_string(main_string, (-1) * shift)


def vigenere_encode_and_decode(my_string, key, state):
    """encode and decode string like vigenere"""
    constant = -1   # for different between encode and decode
    if state == 'encode':
        constant = 1
    length = len(key)
    new_string = []
    for i in range(0, len(my_string)):
        cur_key = key[i % length]
        if (ord(cur_key) >= ord('a')) and (ord(cur_key) <= ord('z')):
            new_string.append(new_char(my_string[i], constant*(ord(cur_key) - ord('a'))))
        elif (ord(cur_key) >= ord('A')) and (ord(cur_key) <= ord('Z')):
            new_string.append(new_char(my_string[i], constant*(ord(cur_key) - ord('A'))))
        else:
            new_string.append(my_string[i])
    return ''.join(new_string)
