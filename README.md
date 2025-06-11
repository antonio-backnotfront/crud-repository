# 🧱 Scalable CLI CRUD User Repository

A modular and extensible Python application for managing user data through a Command-Line Interface (CLI). Built with clean architecture principles, this project is a perfect starting point for scalable systems requiring persistent CRUD operations.

---

## 🚀 Features

- 🔄 **Full CRUD Functionality**: Create, Read, Update, and Delete users.
- ✅ **Input Validation**: Email, phone, age, and uniqueness checks via a dedicated validation module.
- 📁 **JSON Persistence**: User data is stored in a persistent JSON file.
- 🧩 **Plug & Play Architecture**: Easily swap the data backend (e.g., switch from JSON to SQL or Firebase).
- 📦 **Scalable Structure**: Repository, domain, and validators are separated for clean scaling.

---

## 🏗️ Project Structure

```bash
crud_repository/
├── main.py # CLI logic and menu
├── domain/
│ └── User.py # User model
├── validators/
│ └── UserValidators.py # Field validators (email, phone, etc.)
├── interfaces/
│ └── AbstractUserRepository.py # Repository interface (Abstract version of any repository)
├── infrastructure/
│ └── JsonUserRepository.py # JSON-based data repository
├── data/
│ └── data.json # Data file for persistent storage
```

---

## 📚 Quick Documentation

### ✅ Creating a User
Prompts for:
- `Username` (must be unique)
- `Email` (validated format)
- `Full name`
- `Phone` (e.g., `+1234567890`)
- `Age` (non-negative integer)


### 🧪 Validators
#### All user input is validated before submission:
```bash
Email: RFC-compliant
Phone: Must start with +, contain 7–15 digits
Age: Must be a non-negative integer
Username: Must be unique (checked in repository)
```

---
# ➡️ Getting started
```bash
# Clone this repository
git clone https://github.com/antonio-backnotfront/crud-repository.git
cd crud-repository

# Run the app
python3 main.py
```

# 📄 License

MIT License. Use freely in personal or commercial projects.