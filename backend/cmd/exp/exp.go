package main

import (
	"database/sql"
	"fmt"

	_ "github.com/jackc/pgx/v4/stdlib"
)

type PostgresConfig struct {
	Host     string
	User     string
	Password string
	DBName   string
	SSLMode  string
	Port     string
}

func (c *PostgresConfig) ConnectionString() string {
	return fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		c.Host,
		c.Port,
		c.User,
		c.Password,
		c.DBName,
		c.SSLMode,
	)
}

func main() {
	cfg := PostgresConfig{
		Host:     "localhost",
		User:     "xion",
		Password: "supersecret",
		DBName:   "lenslocked",
		SSLMode:  "disable",
		Port:     "5433",
	}

	fmt.Println(cfg.ConnectionString())
	db, err := sql.Open(
		"pgx",
		cfg.ConnectionString(),
	)
	if err != nil {
		panic(err)
	}

	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	fmt.Println("connected to db")
}
