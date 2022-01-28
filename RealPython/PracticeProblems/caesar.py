""" Caesar Cipher
    A caesar cipher is a simple substitution cipher where each letter of the
    plain text is substituted with a letter found by moving 'n' places down the
    alphabet. For an example, if the input plain text is:
        abcd xyz
    and the shift value, n, is 4. The encrypted text would be:
        efgh bcd
    You are to write a function which accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters being transformed while all
    punctuation and whitespace remains unchanged.
    Note: You can assume the plain text is all lowercase ascii, except for
    whitespace and punctuation.
"""


from string import ascii_lowercase


def caesar(plain_text, shift_num=1):
    result = ""
    
    # my first solution
    # for e in plain_text:
    #     if not e.isalnum():
    #         result += e
    #     elif ord(e) + shift_num < 97:
    #         result += chr(ord(e) + shift_num + 26)
    #     elif ord(e) + shift_num > 122:
    #         result += chr(ord(e) + shift_num - 26)
    #     else: 
    #         result += chr(ord(e) + shift_num)
    # return result

    # second solution
    letters_dict = {}
    letters_list = list(ascii_lowercase)
    letters_dict[0] = 'z'
    for i, e in enumerate(letters_list):
        letters_dict[i+1] = e

    for e in plain_text:
        if not e.isalnum():
            result += e
        else:
            result += letters_dict[(letters_list.index(e) + 1 + shift_num) % 26]
    return result

    # course sollution 1
    # letters = ascii_lowercase
    # mask = letters[shift_num:] + letters[:shift_num]
    # trantab = str.maketrans(letters, mask)
    # return plain_text.translate(trantab)

    # course sollution 2
    # def shift_n(letter, amount):
    #     if letter not in ascii_lowercase:
    #         return letter
    #     new_letter = ord(letter) + amount
    #     while new_letter > ord("z"):
    #         new_letter -= 26
    #     while new_letter < ord("a"):
    #         new_letter += 26
    #     return chr(new_letter)
    # enc_list = [shift_n(letter, amount) for letter in message]
    # return "".join(enc_list)

    # course sollution 3
    # def shift_n(letter, table):
    #     try:
    #         index = ascii_lowercase.index(letter)
    #         return table[index]
    #     except ValueError:
    #         return letter

    # amount = amount % 26
    # table = string.ascii_lowercase[amount:] + string.ascii_lowercase[:amount]
    # enc_list = [shift_n(letter, table) for letter in message]
    # return "".join(enc_list)
