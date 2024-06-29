package main

import "fmt"

// Hard-coded credentials in Go
const (
	username = "admin"
	password = "password123"
)

func authenticate(user, pass string) {
	if user == username && pass == password {
		fmt.Println("Authentication successful!")
	} else {
		fmt.Println("Authentication failed.")
	}
}

func main() {
	// Example usage
	authenticate("admin", "password123")
}
