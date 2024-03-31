package config

import "fmt"

type DBConfig struct {
	Host     string
	Port     string
	User     string
	Password string
	Database string
	Sslmode  string
}

func (c *DBConfig) GetConnectionString() string {
	return fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=%s", c.Host, c.Port, c.User, c.Password, c.Database, c.Sslmode)
}

func GetDBConfig() DBConfig {
	return DBConfig{
		Host:     "localhost",
		Port:     "5432",
		User:     "smartworkout",
		Password: "supersecretpassword1123",
		Database: "smartworkout",
		Sslmode:  "disable",
	}
}
