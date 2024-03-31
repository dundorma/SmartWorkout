package main

import (
	"fmt"
	"net/http"

	"github.com/dundorma/SmartWorkout/controllers"
)

func main() {
	fmt.Println("starting server on port 8080")
	http.ListenAndServe(":8080", controllers.Route())
}
