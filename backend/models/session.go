package models

import "database/sql"

type Session struct {
	ID     int
	UserID int
	// Token is only set when creating a new session, When look up a session
	// This will be left empty, as we only store the hash of a session token
	// in our database and we cannot reverse it into a raw token.
	TokenHash string
}

type SessionService struct {
	DB *sql.DB
}

func (ss *SessionService) Create(userID int) (*Session, error) {
	// TODO: create the session token
	// TODO: Implement SessionService.Create
	return nil, nil
}
