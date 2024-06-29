import subprocess

def execute_command(user_input):
    # Небезопасное использование пользовательского ввода для выполнения команды
    command = "ping " + user_input  
    output = subprocess.check_output(command, shell=True)
    return output

if __name__ == "__main__":
    user_input = input("Введите IP-адрес для пинга: ")
    result = execute_command(user_input)
    print(result.decode('utf-8'))
