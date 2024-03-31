package models

import (
	"database/sql"
	"fmt"

	"github.com/dundorma/SmartWorkout/config"
	_ "github.com/jackc/pgx/v5/stdlib"
)

type User struct {
	ID       int
	Name     string
	Email    string
	Password string
}

// query get user by email using pgx and std sql
func GetUserByEmailPassword(email, password string) (User, error) {
	dbCfg := config.GetDBConfig()
	connStr := dbCfg.GetConnectionString()
	db, err := sql.Open("pgx", connStr)
	if err != nil {
		panic(err)
	}

	defer db.Close()

	err = db.Ping()
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("connected to db")

	// TODO: compare salted password

	// query one record using email
	row := db.QueryRow("SELECT id, name, email, password FROM users WHERE email = $1", email)

	var user User
	err = row.Scan(&user.ID, &user.Name, &user.Email, &user.Password)
	if err != nil {
		fmt.Println(err)
		return user, err
	}

	return user, nil
}
