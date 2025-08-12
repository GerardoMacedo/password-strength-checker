# Password Strength Checker 🔐

A beginner-friendly Python CLI tool that evaluates password strength and suggests improvements.  
Includes a **secure input mode** so your password is never shown on screen.

## Overview
CLI tool that scores password strength and suggests improvements.

This project demonstrates:
- Secure password input using `getpass`
- Basic password strength scoring logic
- Suggestions for improving weak passwords
- Practical use of Python’s `re` module for pattern matching

## Features
- **Length check** — longer passwords get higher scores
- **Character variety check** — encourages lowercase, uppercase, numbers, and symbols
- **Common password detection** — warns against easily guessed passwords
- **Score & verdict** — rates password from *Very weak* to *Very strong*
- **Secure entry** — hides password when typing

## Usage

### 1. Clone the repository
```bash
git clone git@github.com:GerardoMacedo/password-strength-checker.git
cd password-strength-checker


## License
This project is open-source and availableunder the [MIT License](LICENSE).
