package main

import (
	"fmt"
	"net/http"

	"github.com/dundorma/SmartWorkout/controllers"
	"github.com/dundorma/SmartWorkout/migrations"
	"github.com/dundorma/SmartWorkout/models"
	"github.com/dundorma/SmartWorkout/templates"
	"github.com/dundorma/SmartWorkout/views"

	"github.com/go-chi/chi/v5"
	"github.com/gorilla/csrf"
)

func main() {
	// SET UP DATABASE
	cfg := models.DefaultPostgresConfig()
	db, err := models.Open(cfg)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	err = models.MigrateFS(db, migrations.FS, ".")
	if err != nil {
		panic(err)
	}

	// SETUP SERVICES
	userService := models.UserService{
		DB: db,
	}
	sessionService := models.SessionService{
		DB: db,
	}

	// SETUP MIDDLEWARE
	umw := controllers.UserMiddleware{
		SessionService: &sessionService,
	}
	csrfKey := "zTRUrqhAFWSH0NR6SsGpFRQn7KqLEvvh"
	csrfMw := csrf.Protect([]byte(csrfKey), csrf.Secure(false))

	// SETUP CONTROLLERS
	userC := controllers.Users{
		UserService:    &userService,
		SessionService: &sessionService,
	}
	userC.Templates.New = views.Must(views.ParseFS(templates.FS, "signup.html", "tailwind.html"))
	userC.Templates.SignIn = views.Must(views.ParseFS(templates.FS, "signin.html", "tailwind.html"))

	// SETUP ROUTER AND ROUTES
	r := chi.NewRouter()
	r.Use(csrfMw)
	r.Use(umw.SetUser)
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
	r.Get("/signup", userC.New)
	r.Post("/signup", userC.Create)
	r.Get("/signin", userC.SignIn)
	r.Post("/signin", userC.ProcessSignIn)
	r.Post("/signout", userC.ProcessSignOut)
	r.Route("/users/me", func(r chi.Router) {
		r.Use(umw.RequireUser)
		r.Get("/", userC.CurrentUser)
	})
	r.NotFound(func(w http.ResponseWriter, r *http.Request) {
		http.Error(w, "Page not found", http.StatusNotFound)
	})

	// START THE SERVER
	fmt.Println("starting server at port 3000")
	http.ListenAndServe(":3000", r)
}
