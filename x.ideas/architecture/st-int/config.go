package main

import (
	"os"

	"gopkg.in/yaml.v2"
)

type Config struct {
	DB     DB     `yaml:"db"`
	Server Server `yaml:"server"`
}

type DB struct {
	Host     string `yaml:"host"`
	Port     string `yaml:"port"`
	User     string `yaml:"user"`
	Password string `yaml:"password"`
	Name     string `yaml:"name"`
}

type Server struct {
	Host string `yaml:"host"`
	Port string `yaml:"port"`
}

func LoadConfig(filename string) (*Config, error) {
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	c := new(Config)

	err = yaml.Unmarshal(file, c)
	if err != nil {
		return nil, err
	}

	return c, nil
}
