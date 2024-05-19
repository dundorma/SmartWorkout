package models

import (
	"database/sql"
	"fmt"
	"strings"

	"github.com/dundorma/SmartWorkout/config"
	_ "github.com/jackc/pgx/v5/stdlib"
	"golang.org/x/crypto/bcrypt"
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

type UserService struct {
	DB *sql.DB
}

func (us *UserService) Create(email, name, password string) (*User, error) {
	email = strings.ToLower(email)
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		return nil, fmt.Errorf("create user: %w", err)
	}

	passwordHash := string(hashedPassword)
	user := User{
		Email:    email,
		Password: passwordHash,
		Name:     name,
	}
	row := us.DB.QueryRow(`
		INSERT INTO users (email, name, password)
		VALUES ($1, $2, $3) returning id`, email, name, passwordHash)
	err = row.Scan(&user.ID)
	if err != nil {
		return nil, fmt.Errorf("create user: %w", err)
	}

	return &user, nil
}
