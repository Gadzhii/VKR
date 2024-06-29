package main

import (
	"fmt"
	"os/exec"
)

func listDirectory(directory string) {
	// Уязвимая строка
	cmd := exec.Command("sh", "-c", "ls "+directory)
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("Ошибка выполнения команды:", err)
		return
	}
	fmt.Println(string(output))
}

func main() {
	var userInput string
	fmt.Print("Введите директорию: ")
	fmt.Scanln(&userInput)
	listDirectory(userInput)
}
