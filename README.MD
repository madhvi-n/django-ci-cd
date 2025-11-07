# 🧩 Django CI/CD Pipeline Demo

[![Django CI](https://github.com/madhvi-n/django-ci-cd/actions/workflows/django.yml/badge.svg)](https://github.com/madhvi-n/django-ci-cd/actions/workflows/django.yml) [![CodeQL](https://github.com/madhvi-n/django-ci-cd/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/madhvi-n/django-ci-cd/actions/workflows/github-code-scanning/codeql)

This repository demonstrates a complete **CI/CD pipeline for a Django project** using **GitHub Actions**.  
It includes automated testing, linting, formatting, and security scanning — following modern Python best practices.

---

## 🚀 Features

- **Continuous Integration (CI)** via GitHub Actions
  - Runs on Python 3.10, 3.11, and 3.12
  - Installs dependencies and executes Django unit tests
- **Code Quality Enforcement**
  - `flake8` for linting and PEP8 compliance
  - `black` for consistent code formatting
- **Security & Static Analysis**
  - `CodeQL` for detecting code vulnerabilities
- **Dependency Caching** for faster builds
- **Multi-version Testing Matrix** for cross-version compatibility

---

## ⚙️ GitHub Workflows

### 🧪 `django.yml`

Located at `.github/workflows/django.yml`

**Purpose:**  
Runs Django tests and lint checks automatically on every push or pull request to `main`.

**Key steps:**

- Setup Python (3.10, 3.11, 3.12)
- Cache dependencies
- Install packages and run tests (`python manage.py test`)
- Run lint checks with `flake8`

## 🧹 Code Quality Tools

| Tool       | Purpose                | Run Command                                                |
| ---------- | ---------------------- | ---------------------------------------------------------- |
| **flake8** | Linting & style checks | `flake8 --max-line-length=120 --exclude=venv,migrations .` |
| **black**  | Code formatter         | `black .`                                                  |
| **isort**  | Imports sorter         | `isort .`                                                  |

### Local setup for code checks

```bash
pip install flake8 black isort
flake8 .
black .
isort .
```

---

## 🧰 Setup (Local Development)

1. **Clone the repository**

   ```bash
   git clone https://github.com/madhvi-n/django-ci-cd.git
   cd django-ci-cd
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (or venv\Scripts\activate on Windows)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**

   ```bash
   python manage.py test
   ```

---

## 🧪 CI Workflow Status

| Workflow            | Status                                                                                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Django CI**       | [![Django CI](https://github.com/madhvi-n/django-ci-cd/actions/workflows/django.yml/badge.svg)](https://github.com/madhvi-n/django-ci-cd/actions/workflows/django.yml)                                |
| **CodeQL Analysis** | [![CodeQL](https://github.com/madhvi-n/django-ci-cd/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/madhvi-n/django-ci-cd/actions/workflows/github-code-scanning/codeql) |

---

## 🧩 Folder Structure

```
.
├── .github/
│   └── workflows/
│       ├── django.yml
├── app/                  # Django app folder
├── manage.py
├── requirements.txt
├── README.md
└── .flake8               # Lint configuration
```

---

## 🧠 Future Enhancements

- ✅ Add coverage reports (e.g., `coverage.py` + Codecov)
- ✅ Integrate Docker-based testing
- ✅ Deploy to staging via GitHub Actions
