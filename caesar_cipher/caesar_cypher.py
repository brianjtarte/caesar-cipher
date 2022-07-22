from caesar_cipher.clock_queue import Clock_queue
import string

"""
save a list of the alphabet
create a function called encrypt
      takes in two parameters
        phrase(string), num(shift)
the phrase will then be shifted that many letters of the alphabet
shifts that exceed 26 should wrap around.
shifts that push a letter out or range should wrap around.
"""

"""
Create a function called decrypt
    takes in the encrypted message and performs the encrypt but with the negative shift


Create a crack method that brute forces through all the shifts 


"""


# create alphabet

# create encrypt function
def encrypt(phrase=None, shift=None):
    alphabet = Clock_queue()
    secret_message = ''
    # the encryption clock

    lower_alphabets = list(string.ascii_lowercase)
    upper_alphabets = list(string.ascii_uppercase)
    alphalist = ['1', '.', ',', '!']
    for lower in lower_alphabets:
        upper_alphabets.append(lower)
        print(upper_alphabets)
    for symbol in alphalist:
        upper_alphabets.append(symbol)

    for letter in upper_alphabets:
        alphabet.enqueue(letter, 'r')

    for unchanged_letter in phrase:
        encrypted_letter = alphabet.clock_wise(unchanged_letter, shift)
        secret_message += encrypted_letter

    return secret_message


def decrypt(phrase=None, shift=None):
    alphabet = Clock_queue()
    decrypt_msg = ''
    if phrase.islower():
        whole_alphabets = list(string.ascii_lowercase)
    else:
        whole_alphabets = list(string.ascii_uppercase)
    for letter in whole_alphabets:
        alphabet.enqueue(letter, 'r')

    for letter in phrase:
        d = alphabet.counter_clock_wise(letter, shift)
        decrypt_msg += d
    return decrypt_msg


def crack():
    pass


if __name__ == "__main__":
    list1 = 'Hello woRld !'
    print(encrypt(list1, 4))
