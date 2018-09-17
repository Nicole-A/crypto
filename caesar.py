from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ''
    for char in text:
        if (char.isalpha()):
            new_text = new_text + rotate_character(char,rot)
        else:
            new_text = new_text + char
    return new_text

    
def main():

    user_letter = (input("Type a message:"))
    user_number = (input("Rotate by:"))

    print((encrypt(user_letter, user_number)))

if __name__ == "__main__":
    main()