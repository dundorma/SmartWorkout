package main

import (
	"fmt"
	"net/http"

	"github.com/dundorma/SmartWorkout/controllers"
	"github.com/dundorma/SmartWorkout/models"
	"github.com/dundorma/SmartWorkout/templates"
	"github.com/dundorma/SmartWorkout/views"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/gorilla/csrf"
)

func main() {
	r := chi.NewRouter()
	r.Use(middleware.Logger)

	r.Get(
		"/",
		controllers.StaticHandler(
			views.Must(views.ParseFS(templates.FS, "home.html", "tailwind.html")),
		),
	)
	r.Get(
		"/contact",
		controllers.StaticHandler(
			views.Must(views.ParseFS(templates.FS, "contact.html", "tailwind.html")),
		),
	)
	r.Get(
		"/faq",
		controllers.FAQ(views.Must(views.ParseFS(templates.FS, "faq.html", "tailwind.html"))),
	)

	cfg := models.DefaultPostgresConfig()
	db, err := models.Open(cfg)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	userService := models.UserService{
		DB: db,
	}

	userC := controllers.Users{
		UserService: &userService,
	}

	userC.Templates.New = views.Must(views.ParseFS(templates.FS, "signup.html", "tailwind.html"))
	userC.Templates.SignIn = views.Must(views.ParseFS(templates.FS, "signin.html", "tailwind.html"))

	r.Get("/signup", userC.New)
	r.Post("/signup", userC.Create)
	r.Get("/signin", userC.SignIn)
	r.Post("/signin", userC.ProcessSignIn)
	r.Get("/users/me", userC.CurrentUser)

	csrfKey := "zTRUrqhAFWSH0NR6SsGpFRQn7KqLEvvh"
	csrfMw := csrf.Protect([]byte(csrfKey), csrf.Secure(false))

	fmt.Println("starting server at port 3000")
	http.ListenAndServe(":3000", csrfMw(r))
}
