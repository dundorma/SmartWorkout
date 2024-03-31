package controllers

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

type Login struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

func Route() *chi.Mux {
	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Welcome to SmartWorkout"))
	})

	r.Post("/login", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")

		var u Login
		json.NewDecoder(r.Body).Decode(&u)
		fmt.Printf("The user request value %v", u)

		if u.Email == "test" && u.Password == "test" {
			jwtToken := GetJwtConfig()
			token, err := jwtToken.CreateToken(u.Email)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			w.WriteHeader(http.StatusOK)
			w.Write([]byte(`{"message": "success", "token": "` + token + `"}`))
		} else {
			w.WriteHeader(http.StatusUnauthorized)
			w.Write([]byte(`{"message": "unauthorized"}`))
		}
	})

	r.Route("/protected", func(r chi.Router) {
		r.Use(ProtectedHandler())
		r.Get("/", func(w http.ResponseWriter, r *http.Request) {
			w.Write([]byte("Welcome to Protected"))
		})
	})

	return r
}
