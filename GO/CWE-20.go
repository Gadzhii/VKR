package main

import (
	"fmt"
	"net/http"
	"strconv"
)

func main() {
	http.HandleFunc("/divide", divideHandler)
	http.ListenAndServe(":8080", nil)
}

func divideHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	aStr := query.Get("a")
	bStr := query.Get("b")

	// Уязвимость: отсутствие проверки корректности входных данных
	a, err := strconv.Atoi(aStr)
	if err != nil {
		http.Error(w, "Invalid parameter 'a'", http.StatusBadRequest)
		return
	}

	b, err := strconv.Atoi(bStr)
	if err != nil {
		http.Error(w, "Invalid parameter 'b'", http.StatusBadRequest)
		return
	}

	// Уязвимость: отсутствие проверки деления на ноль
	result := a / b

	fmt.Fprintf(w, "Result: %d", result)
}
