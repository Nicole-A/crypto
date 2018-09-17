def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet.upper()
    if letter in alphabet:
        letter_number = alphabet.index(letter)
    if letter in alphabet_upper:
        letter_number = alphabet_upper.index(letter)     
    return letter_number

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a_char = alphabet_position(char)
    new_char = a_char + int(rot)
    for number in char:
      if new_char > 25:
        new_char = new_char % 26
    if char.isupper():
      return alphabet[new_char].upper()
    else:
      return alphabet[new_char]
