package models

import (
	"database/sql"
	"fmt"
	"strings"

	"golang.org/x/crypto/bcrypt"
)

type User struct {
	ID       int
	Email    string
	Name     string
	Password string
}

type UserService struct {
	DB *sql.DB
}

type NewUser struct {
	Email    string
	Name     string
	Password string
}

func (us *UserService) Create(email, name, password string) (*User, error) {
	email = strings.ToLower(email)
	hashedBytes, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	passwordHash := string(hashedBytes)
	if err != nil {
		return nil, fmt.Errorf("Create user (hashing password): %w", err)
	}
	user := User{
		Email:    email,
		Name:     name,
		Password: passwordHash,
	}

	row := us.DB.QueryRow(`
		INSERT INTO users (email, name, password)
		VALUES ($1, $2, $3) RETURNING id`, email, name, passwordHash)
	err = row.Scan(&user.ID)
	if err != nil {
		return nil, fmt.Errorf("Create user (inserting into users): %w", err)
	}

	return &user, nil
}

func (us *UserService) Update(user *User) error {
	return nil
}

func (us *UserService) Authenticate(email, password string) (*User, error) {
	email = strings.ToLower(email)
	user := User{
		Email: email,
	}

	row := us.DB.QueryRow(`SELECT id, name, password FROM users WHERE email=$1`, email)
	err := row.Scan(&user.ID, &user.Name, &user.Password)
	if err != nil {
		return nil, fmt.Errorf("authenticate (query): %w", err)
	}

	err = bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(password))
	if err != nil {
		return nil, fmt.Errorf("authenticate (compare): %w", err)
	}

	return &user, nil
}
