package main

import (
	"fmt"
	"net/http"
)

// Функция-обработчик для защищенного ресурса
func protectedResource(w http.ResponseWriter, r *http.Request) {
	user := r.URL.Query().Get("user")
	if user == "" {
		http.Error(w, "User not specified", http.StatusBadRequest)
		return
	}

	// Не проверяется подлинность пользователя
	fmt.Fprintf(w, "Access granted to user: %s", user)
}

func main() {
	http.HandleFunc("/protected", protectedResource)
	fmt.Println("Server started at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
