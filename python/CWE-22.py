import os

def read_file(filename):
    # Предполагаем, что filename получен от пользователя или из другого источника
    file_path = "/var/www/uploads/" + filename  # Пример потенциально уязвимой строки

    # Проверяем, что путь начинается с ожидаемой директории
    if file_path.startswith("/var/www/uploads/"):
        try:
            with open(file_path, 'r') as f:
                contents = f.read()
                print("Содержимое файла:", contents)
        except FileNotFoundError:
            print("Файл не найден")
        except IOError:
            print("Ошибка при чтении файла")
    else:
        print("Недопустимый путь к файлу")

# Пример вызова функции с контролируемым пользователем вводом
filename = "../../../../../etc/passwd"  # Пользовательский ввод, который может привести к обходу пути
read_file(filename)