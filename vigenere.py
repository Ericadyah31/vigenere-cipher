def encrypt_vigenere(plain_text, key):
    encrypted_message = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            if char.isupper():
                shift = ord('A')
            else:
                shift = ord('a')
            encrypted_message += chr((ord(char) + ord(key_char) - 2 * shift) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_vigenere(encrypted_text, key):
    decrypted_message = ""
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            if char.isupper():
                shift = ord('A')
            else:
                shift = ord('a')
            decrypted_message += chr((ord(char) - ord(key_char) + 26) % 26 + shift)
        else:
            decrypted_message += char
    return decrypted_message


# Contoh penggunaan
plain_text = "Hello"
key = "Vigenere"

encrypted_text = encrypt_vigenere(plain_text, key)
decrypted_text = decrypt_vigenere(encrypted_text, key)

print("Pesan Asli: " + plain_text)
print("Pesan Terenkripsi: " + encrypted_text)
print("Pesan Terdekripsi: " + decrypted_text)