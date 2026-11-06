def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))

ciphertext = encrypt(message, shift)
plaintext = decrypt(ciphertext, shift)

print("\nPlaintext :", message)
print("Ciphertext:", ciphertext)
print("Decrypted :", plaintext)
