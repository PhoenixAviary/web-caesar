def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter.isupper():
        position = alphabet_up.find(letter)
    elif letter.islower():
        position = alphabet.find(letter)
    else:
        position = 27
    return position



def rotate_character(char, rot):
    current_position = alphabet_position(char)
    if current_position == 27:
        return char
    else:
        new_position = current_position + int(rot)
        alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if char.isupper():
            alphabet = alphabet_up
        else:
            char.islower()
            alphabet = alphabet_low

        if new_position < 26:
            jumbled_letter = alphabet[new_position]
        else:
            jumbled_letter = alphabet[new_position % 26]
        return jumbled_letter




def encrypt(message, rotate):
    encrypted = ""
    for char in message:
        encrypted = encrypted + rotate_character(char, rotate)
    return (encrypted)
