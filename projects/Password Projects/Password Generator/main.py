import random
import string


def main():
    print("_____________________________________")
    print("| Welcome to this Password Generator |")
    print("-------------------------------------\n")
    try:
        length = int(
            input("how long do you want your password to be (minimum of 8 number)")
        )
    except:
        print("Input numners only")
    password_length = 0
    while password_length < length:
        print("Your password must have at least 8 characters")
        password_length = getPasswordLength()

    all_characters = getCharacters()
    password = generatePassword(all_characters, password_length)
    print("\nYour password is: " + password)
    print("__________________________________________")
    print("| Thanks for using the Password Generator |")
    print("------------------------------------------")


def getPasswordLength():
    return int(input("\nEnter the length of password: "))


def getCharacters():
    # define the characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    return lower + upper + num + symbols


def generatePassword(all_characters, password_length):
    return "".join(random.sample(all_characters, password_length))


main()
