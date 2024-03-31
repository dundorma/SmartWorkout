package controllers

import (
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

type JwtToken struct {
	SecretKey string
}

func (j *JwtToken) CreateToken(email string) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"email": email,
		"exp":   time.Now().Add(time.Hour * 24).Unix(),
	})

	tokenString, err := token.SignedString([]byte(j.SecretKey))
	if err != nil {
		return "", err
	}

	return tokenString, nil
}

func (j *JwtToken) ParseToken(tokenString string) error {
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return []byte(j.SecretKey), nil
	})
	if err != nil {
		return err
	}

	if !token.Valid {
		return fmt.Errorf("Token is Invalid")
	}

	return nil
}

func GetJwtConfig() JwtToken {
	return JwtToken{
		SecretKey: "supersecretkey",
	}
}
