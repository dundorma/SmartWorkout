package models

import (
	"database/sql"
	"fmt"

	"github.com/dundorma/SmartWorkout/rand"
)

const (
	// The minimum number of bytes to be used for each session token
	MinBytesPerToken = 32
)

type Session struct {
	ID     int
	UserID int
	// Token is only set when creating a new session, When look up a session
	// This will be left empty, as we only store the hash of a session token
	// in our database and we cannot reverse it into a raw token.
	Token     string
	TokenHash string
}

type SessionService struct {
	DB            *sql.DB
	BytesPerToken int
}

func (ss *SessionService) Create(userID int) (*Session, error) {
	bytesPerToen := ss.BytesPerToken
	if bytesPerToen < MinBytesPerToken {
		bytesPerToen = MinBytesPerToken
	}

	token, err := rand.String(bytesPerToen)
	if err != nil {
		return nil, fmt.Errorf("create: %w", err)
	}
	// TODO: Hash the session token
	session := Session{
		UserID: userID,
		Token:  token,
		// TODO: set TOkenHash
	}
	// TODO: Store session to DB
	// TODO: Implement SessionService.Create
	return &session, nil
}

func (ss *SessionService) User(token string) (*User, error) {
	return nil, nil
}
