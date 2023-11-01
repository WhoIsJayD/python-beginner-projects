import string

# Constants
acentos = "óá"
exceptions = "_ "
sequenceNumbers = "0123456789"
sequenceAlphabet = string.ascii_lowercase
controller = False


# METHODS VERIFY IF PASS IS STRONG
def numberOfCharacters(password):
    return len(password) * 4


def upperCaseLetters(password):
    charsUpper = 0
    if not password.isupper():
        for i in password:
            if i.isupper():
                charsUpper += 1

        if charsUpper != 0:
            charsUpper = (len(password) - charsUpper) * 2
    return charsUpper


def lowerCaseLetters(password):
    charsLower = 0
    if password.islower():
        for i in password:
            if i.islower() and i not in acentos:
                charsLower += 1

        if charsLower != 0:
            charsLower = (len(password) - charsLower) * 2
    return charsLower


def numbers(password):
    charsNumber = 0
    if not password.isdigit():
        for i in password:
            if i.isdigit():
                charsNumber += 1
    return charsNumber * 4


def symbols(password):
    charsSymbol = sum(
        1
        for i in password
        if (
            i.lower() not in sequenceAlphabet
            and i not in exceptions
            and i not in sequenceNumbers
        )
    )
    return charsSymbol * 6


def middleNumberOrSymbol(password):
    CharsMiddle = sum(
        1
        for i in range(1, len(password))
        if (
            password[i].isdigit()
            or (
                password[i].lower() not in sequenceAlphabet
                and password[i] not in exceptions
            )
        )
        and i != len(password) - 1
    )
    return CharsMiddle * 2


def requirements(password):
    requirementsCount = 0

    if len(password) >= 8:
        requirementsCount += 1

        if upperCaseLetters(password) > 0:
            requirementsCount += 1

        if lowerCaseLetters(password) > 0:
            requirementsCount += 1

        if numbers(password) > 0:
            requirementsCount += 1

        if symbols(password) > 0:
            requirementsCount += 1

        if requirementsCount == 4:
            requirementsCount *= 2
        else:
            requirementsCount = 0

    return requirementsCount


def lettersOnly(password):
    countDigit = sum(1 for i in password if i.isdigit())
    countDigit = len(password) * -1 if countDigit == 0 else 0
    return countDigit


def numbersOnly(password):
    countLetters = sum(1 for i in password if i.isalpha())
    if countLetters == 0:
        return len(password) * -1
    else:
        countLetters = 0

    return countLetters


def consecutiveLowerCase(password):
    password = f"{password}1"

    countLowerCase = sum(
        1
        for i in range(len(password))
        if (
            password[i].islower()
            and password[i + 1].islower()
            and password[i + 1] not in acentos
            and password[i] not in acentos
        )
    )
    return (countLowerCase * 2) * -1


def consecutiveUpperCase(password):
    password = f"{password}1"

    countUpperCase = sum(
        1
        for i in range(len(password))
        if password[i].isupper() and password[i + 1].isupper()
    )
    return (countUpperCase * 2) * -1


def consecutiveNumbers(password):
    password = f"{password}a"

    countNumbers = sum(
        1
        for i in range(len(password))
        if password[i].isdigit() and password[i + 1].isdigit()
    )
    return (countNumbers * 2) * -1


def sequentialNumbers(password):
    numbers = ""
    countNumbers = 0

    for i in range(len(password)):
        numbers += password[i : i + 3]

        if numbers in sequenceNumbers and len(numbers) == 3:
            countNumbers += 1

        numbers = ""

    return (countNumbers * 3) * -1


def sequentialLetters(password):
    letters = ""
    countLetters = 0

    for i in range(len(password)):
        letters += password[i : i + 3]

        if letters in sequenceAlphabet and len(letters) == 3:
            countLetters += 1

        letters = ""

    return (countLetters * 3) * -1
