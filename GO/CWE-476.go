package main

import (
	"fmt"
	"net/http"
)

func HandleRequest(client http.Client, request *http.Request) (*http.Response, error) {
	response, err := client.Do(request)
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	// Предположим, здесь есть код, который обрабатывает ответ
	// Например:
	// _, _ = ioutil.ReadAll(response.Body)

	return response, nil
}

func main() {
	// Создаем HTTP клиент
	client := http.Client{}

	// Передаем nil в качестве запроса, что может привести к разыменованию nil указателя
	_, err := HandleRequest(client, nil)
	if err != nil {
		fmt.Println("Error:", err)
	}
}
