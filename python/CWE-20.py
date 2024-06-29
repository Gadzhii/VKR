def get_user_input():
    user_input = input("Введите число от 1 до 10: ")
    return user_input

def process_input(user_input):
    # Уязвимость: неправильная проверка ввода
    number = int(user_input)
    if number < 1 or number > 10:
        print("Недопустимое число!")
    else:
        print(f"Допустимое число: {number}")

def main():
    user_input = get_user_input()
    process_input(user_input)

if __name__ == "__main__":
    main()
