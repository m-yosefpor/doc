package main

import "gorm.io/gorm"

type Contact struct {
	gorm.Model
	FirstName    string   `json:"firstName"`
	LastName     string   `json:"lastName"`
	PhoneNumbers []string `json:"phoneNumbers" gorm:"type:text[]"`
	Email        string   `json:"email"`
	Address      string   `json:"address"`
}
