package main

import (
	"fmt"
	"sync"
)

func safeGoRoutine(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println("This is a safe goroutine example.")
}

func main() {
	var wg sync.WaitGroup
	wg.Add(1)
	go safeGoRoutine(&wg)
	wg.Wait()
}
