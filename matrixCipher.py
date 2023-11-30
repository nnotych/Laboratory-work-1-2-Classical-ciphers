# Columnar Transposition
import math

# Задаємо ключ для шифрування
key = "KEY"

# Функція для шифрування повідомлення
def encryptMessage(msg):
    cipher = ""  # Змінна для збереження зашифрованого повідомлення
    
    # Відстеження індексів ключа
    k_indx = 0
    
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    
    # Обчислення кількості стовпців у матриці
    col = len(key)
    
    # Обчислення максимальної кількості рядків у матриці
    row = int(math.ceil(msg_len / col))
    
    # Додавання символу-заповнювача '_' у порожні
    # комірки матриці
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    
    # Створення матриці та вставка повідомлення та
    # символів-заповнювачів рядками
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    
    # Читання матриці по стовпцях, використовуючи ключ
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    
    return cipher

#ВідкритеПовідомлення
msg = "Hello Nikita"

# Виклик функції для шифрування
cipher = encryptMessage(msg)

# Виведення зашифрованого повідомлення
print("Encrypted Message: {}".format(cipher))

