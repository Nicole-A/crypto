from helpers import alphabet_position, rotate_character
def encrypt(text, word):
    new_text = ''
    ind = 0
    for char in text:
        char_rotation = alphabet_position(word[ind])
        if (char.isalpha()):
          if ind >= (len(word)-1):
              ind = 0
          else:
              ind = ind + 1
          new_text = new_text + rotate_character(char,char_rotation)
        else:
          new_text = new_text + char
    return new_text

    
def main():

    user_letter = (input("Type a message:"))
    user_word = (input("Encryption key:"))

    print((encrypt(user_letter, user_word)))

if __name__ == "__main__":
    main()