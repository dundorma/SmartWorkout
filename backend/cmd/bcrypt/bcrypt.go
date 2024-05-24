package main

import (
	"fmt"
	"os"
	"strings"

	"golang.org/x/crypto/bcrypt"
)

func handleHash(password string) {
	fmt.Println(password)
	hashed, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		fmt.Printf("error hashing password %v\n", password)
		return
	}

	fmt.Println(string(hashed))
}

func handleCompare(password string, hash string) {
	fmt.Println(password, hash)
	if bcrypt.CompareHashAndPassword([]byte(hash), []byte(password)) != nil {
		if bcrypt.CompareHashAndPassword([]byte(password), []byte(hash)) == nil {
			fmt.Println("Password matches hash")
			return
		}
		fmt.Println("Password does not match hash")
	} else {
		fmt.Println("Password matches hash")
	}
}

func main() {
	if len(os.Args) <= 2 {
		fmt.Println("Usage: bcrypt hash \"password\"")
		fmt.Println("Usage: bcrypt compare \"password\" \"hash\"")
		os.Exit(1)
	}

	option := strings.ToLower(os.Args[1])
	switch option {
	case "hash":
		if len(os.Args) != 3 {
			fmt.Println("Usage: bcrypt hash \"password\"")
			os.Exit(1)
		} else {
			handleHash(os.Args[2])
		}
	case "compare":
		if len(os.Args) != 4 {
			fmt.Println("Usage: bcrypt compare \"password\" \"hash\"")
			os.Exit(1)
		} else {
			handleCompare(os.Args[2], os.Args[3])
		}
	default:
		println("invalid option or your arguments has too much or too low of a value")
	}
}
