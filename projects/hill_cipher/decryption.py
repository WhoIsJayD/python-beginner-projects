import mysql.connector as c

con = c.connect(host="localhost", user="root", password="password@123")
cur = con.cursor()
cur.execute("use password_manager")


# to perform the modulus operation
def mod(num):
    return 26 - (abs(num) % 26) if num < 0 else num % 26


def hill_cipher(text, key_matrix):
    sum = 0
    for i in range(3):
        sum += (text[i] - 1) * key_matrix[i]
    cipher_text = [sum]
    sum = 0
    for i in range(3, 6):
        sum += (text[i - 3] - 1) * key_matrix[i]
    cipher_text.append(sum)

    sum = 0
    for i in range(6, 9):
        sum += (text[i - 6] - 1) * key_matrix[i]
    cipher_text.append(sum)
    return cipher_text


def message(actual_text):
    HillCipherText = " "
    matrix = []
    sect = [actual_text[i] for i in range(3)]
    for i in range(3):
        cur.execute(f"select lid from loalpha where lchar = '{sect[i]}'")
        l = cur.fetchone()
        matrix.extend(iter(l))
    l = [4, 15, 24, 9, 17, 0, 15, 6, 17]
    h = hill_cipher(matrix, l)

    for i in h:
        r = mod(i)
        cur.execute(f"select lchar from loalpha where lid = {r + 1}")
        t = cur.fetchone()

        HillCipherText += t[0]

    return HillCipherText


if __name__ == "__main__":
    a = input("enter the coded text: ")
    print(message(a))
