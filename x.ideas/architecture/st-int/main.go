package main

import (
	"log/slog"
	"net"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
	_ "go.uber.org/automaxprocs"
	"gorm.io/gorm"
)

type ContactHandler struct {
	DB     *gorm.DB
	Logger *slog.Logger
}

func main() {

	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))

	config, err := LoadConfig("config.yaml")
	if err != nil {
		logger.Error("Failed to load config:", "error", err)
		os.Exit(1)
	}

	db, err := ConnectDatabase(config.DB)
	if err != nil {
		logger.Error("failed to create db", "error", err)
		//os.Exit(1)
	}

	handler := &ContactHandler{
		DB:     db,
		Logger: logger,
	}

	e := echo.New()
	e.POST("/contacts", handler.CreateContact)

	serverAddr := net.JoinHostPort(config.Server.Host, config.Server.Port)
	if err := e.Start(serverAddr); err != http.ErrServerClosed {
		handler.Logger.Error("server error", err)
	}
}

func (h *ContactHandler) CreateContact(c echo.Context) error {
	contact := &Contact{}
	if err := c.Bind(contact); err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, err.Error())
	}

	result := h.DB.Create(&contact)
	if result.Error != nil {
		h.Logger.Warn("create contact failed", "id", contact.ID, "error", result.Error.Error())
		return echo.NewHTTPError(http.StatusInternalServerError, "create contact failed")
	}
	slog.Info("Created new contact", "id", contact.ID)
	return c.JSON(http.StatusCreated, contact)
}
