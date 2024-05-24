package main

import (
	"database/sql"
	"fmt"

	"github.com/dundorma/SmartWorkout/models"

	_ "github.com/jackc/pgx/v4/stdlib"
)

func main() {
	cfg := fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		"localhost",
		"5432",
		"xion",
		"supersecret",
		"lenslocked",
		"disable",
	)

	db, err := sql.Open("pgx", cfg)
	if err != nil {
		panic(err)
	}

	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}
	us := models.UserService{
		DB: db,
	}

	user, err := us.Create("bob@bob.com", "bob123")
	if err != nil {
		panic(err)
	}

	fmt.Println(user)
}
