P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def left_shift(bits, count):
    return bits[count:] + bits[:count]


def generate_keys(key):
    key = permute(key, P10)
    left = key[:5]
    right = key[5:]
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    key1 = permute(left + right, P8)
    left = left_shift(left, 2)
    right = left_shift(right, 2)
    key2 = permute(left + right, P8)
    return key1, key2


def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))


def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    value = box[row][col]
    return format(value, '02b')


def fk(bits, key):
    left = bits[:4]
    right = bits[4:]
    expanded = permute(right, EP)
    temp = xor(expanded, key)
    left_sbox = sbox(temp[:4], S0)
    right_sbox = sbox(temp[4:], S1)
    combined = permute(left_sbox + right_sbox, P4)
    new_left = xor(left, combined)
    return new_left + right


def switch(bits):
    return bits[4:] + bits[:4]


def encrypt_block(bits, key1, key2):
    bits = permute(bits, IP)
    bits = fk(bits, key1)
    bits = switch(bits)
    bits = fk(bits, key2)
    return permute(bits, IP_INV)


def decrypt_block(bits, key1, key2):
    bits = permute(bits, IP)
    bits = fk(bits, key2)
    bits = switch(bits)
    bits = fk(bits, key1)
    return permute(bits, IP_INV)


def encrypt_byte(byte, key1, key2):
    bits = format(byte, '08b')
    encrypted = encrypt_block(bits, key1, key2)
    return int(encrypted, 2)


def decrypt_byte(byte, key1, key2):
    bits = format(byte, '08b')
    decrypted = decrypt_block(bits, key1, key2)
    return int(decrypted, 2)


def encrypt_data(data, key):
    key1, key2 = generate_keys(key)
    return bytes(encrypt_byte(byte, key1, key2) for byte in data)


def decrypt_data(data, key):
    key1, key2 = generate_keys(key)
    return bytes(decrypt_byte(byte, key1, key2) for byte in data)


if __name__ == "__main__":
    key = input("Enter 10-bit key: ")

    if len(key) != 10 or any(c not in "01" for c in key):
        print("Invalid key. Enter exactly 10 binary digits.")
        exit()

    message = input("Enter message: ")
    data = message.encode()
    encrypted = encrypt_data(data, key)
    decrypted = decrypt_data(encrypted, key)

    print("\nPlaintext :", message)
    print("Ciphertext:", encrypted.hex())
    print("Decrypted :", decrypted.decode())
