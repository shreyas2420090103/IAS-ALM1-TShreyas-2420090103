def create_matrix(key):
    key = key.upper().replace("J", "I")
    letters = []

    for char in key:
        if char.isalpha() and char not in letters:
            letters.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in letters:
            letters.append(char)

    return [letters[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def prepare_text(text):
    text = ''.join(c for c in text.upper() if c.isalpha())
    text = text.replace("J", "I")

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def encrypt(text, matrix):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
message = input("Enter plaintext: ")

matrix = create_matrix(key)
ciphertext = encrypt(message, matrix)

print("\nPlayfair Matrix:")

for row in matrix:
    print(" ".join(row))

print("\nPlaintext :", message)
print("Ciphertext:", ciphertext)
