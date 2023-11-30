def encrypt_vigenere_ukrainian(plaintext, key):
    # Створення алфавіту для української мови
    ukr_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    # Перетворення тексту і ключа у великі літери
    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = ''
    key_length = len(key)
    ukr_alphabet_len = len(ukr_alphabet)

    for i in range(len(plaintext)):
        if plaintext[i] in ukr_alphabet:
            # Знаходження індексів букв у тексті та ключі
            plaintext_index = ukr_alphabet.index(plaintext[i])
            key_index = ukr_alphabet.index(key[i % key_length])

            # Зашифрування букви та додавання до результату
            encrypted_index = (plaintext_index + key_index) % ukr_alphabet_len
            ciphertext += ukr_alphabet[encrypted_index]
        else:
            # Якщо символ не є літерою, додаємо його без змін
            ciphertext += plaintext[i]

    return ciphertext

def decrypt_vigenere_ukrainian(ciphertext, key):
    # Створення алфавіту для української мови
    ukr_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    # Перетворення тексту і ключа у великі літери
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ''
    key_length = len(key)
    ukr_alphabet_len = len(ukr_alphabet)

    for i in range(len(ciphertext)):
        if ciphertext[i] in ukr_alphabet:
            # Знаходження індексів букв у тексті та ключі
            ciphertext_index = ukr_alphabet.index(ciphertext[i])
            key_index = ukr_alphabet.index(key[i % key_length])

            # Розшифрування букви та додавання до результату
            decrypted_index = (ciphertext_index - key_index) % ukr_alphabet_len
            plaintext += ukr_alphabet[decrypted_index]
        else:
            # Якщо символ не є літерою, додаємо його без змін
            plaintext += ciphertext[i]

    return plaintext

# Приклад використання:
plaintext = "нікіта"
key = "КЛЮЧ"
ciphertext = encrypt_vigenere_ukrainian(plaintext, key)
decrypted_text = decrypt_vigenere_ukrainian(ciphertext, key)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)