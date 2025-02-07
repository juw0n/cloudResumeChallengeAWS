package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"gopkg.in/gomail.v2"
)

// Validate environment variables
func validateEnvVars() {
	requiredVars := []string{"GMAIL_USERNAME", "GMAIL_PASSWORD"}
	for _, envVar := range requiredVars {
		if os.Getenv(envVar) == "" {
			log.Fatalf("Environment variable %s is not set", envVar)
		}
	}
}

func sendEmail(to, subject, body string) error {
	// Get environment variables (more secure than hardcoding credentials)
	smtpServer := "smtp.gmail.com"
	smtpPort := 587
	senderEmail := os.Getenv("GMAIL_USERNAME")
	senderPassword := os.Getenv("GMAIL_PASSWORD")

	// Create a new email message
	msg := gomail.NewMessage()
	msg.SetHeader("From", senderEmail)
	msg.SetHeader("To", to)
	msg.SetHeader("Subject", subject)
	msg.SetBody("text/plain", body)

	// Set up the SMTP dialer
	dialer := gomail.NewDialer(smtpServer, smtpPort, senderEmail, senderPassword)

	// Send the email
	if err := dialer.DialAndSend(msg); err != nil {
		return fmt.Errorf("failed to send email: %v", err)
	}

	log.Println("Email sent successfully to:", to)
	return nil
}

// Handler function to process contact form submissions
func contactFormHandler(ctx *gin.Context) {
	type ContactForm struct {
		Name    string `json:"name" binding:"required"`
		Email   string `json:"email" binding:"required"`
		Subject string `json:"subject" binding:"required"`
		Message string `json:"message" binding:"required"`
	}
	var form ContactForm

	// Bind JSON request body to struct
	if err := ctx.ShouldBindJSON(&form); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "Invalid Inputs"})
		return
	}

	// Send the email
	to := "oduns07@gmail.com"
	subject := form.Subject
	body := "From: " + form.Name + "\nEmail: " + form.Email + "\n\nMessage:\n" + form.Message

	if err := sendEmail(to, subject, body); err != nil {
		log.Printf("Failed to send email: %v", err)
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to send email"})
		return
	}

	ctx.JSON(http.StatusOK, gin.H{"message": "Email sent successfully!"})

}

func main() {

	validateEnvVars()
	router := gin.Default()
	router.POST("/contact", contactFormHandler)

	log.Println("Server started on port :8080")

	if err := router.Run(":8080"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}

}
