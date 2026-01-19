# SIFRA Project Context

## Project Overview
SIFRA (Sistema Integrado de Frequência e Assiduidade) is a full-stack application for managing school attendance.
**Note:** The project's `README.md` currently describes a Java Spring Boot backend, but the actual `backend/` directory contains a **Python FastAPI** application. This document reflects the actual codebase state.

## 📂 Directory Structure

| Directory | Description | Technology |
| :--- | :--- | :--- |
| `frontend/` | The web user interface. | React 19, Axios, React Router 7 |
| `backend/` | The application server. | Python 3.13, FastAPI, SQLModel, UV |

---

## 🚀 Getting Started

### 1. Backend (Python FastAPI)
The backend is managed by `uv`.

*   **Directory:** `backend/`
*   **Prerequisites:** Python 3.13+, `uv` (project manager).
*   **Installation:**
    ```bash
    cd backend
    uv sync
    ```
*   **Running:**
    ```bash
    uv run fastapi dev src/main.py
    ```
    *   Server runs on: `http://localhost:8000` (by default)
    *   API Docs: `http://localhost:8000/docs`
*   **Configuration:**
    *   Create a `.env` file in `backend/` based on `.env.example`.
    *   Key settings: `DATABASE_URL`, `SECRET_KEY`.

### 2. Frontend (React)
*   **Directory:** `frontend/`
*   **Prerequisites:** Node.js (v18+ recommended)
*   **Installation:**
    ```bash
    cd frontend
    npm install
    ```
*   **Running:**
    ```bash
    npm start
    ```
    *   Access at: `http://localhost:3000`

---

## ⚠️ Important Configuration Notes

### API Connection
The frontend is currently configured to connect to a **remote server** (`http://5.78.68.22:5070/api/v1`) in `frontend/src/service/api.js`.

To connect to your **local backend**, you must update `frontend/src/service/api.js`:
```javascript
// Change this:
// baseURL: "http://5.78.68.22:5070/api/v1",

// To this (assuming local backend on port 8000):
baseURL: "http://localhost:8000/api/v1",
```

---

## 🛠 Development Conventions

### Backend (Python)
*   **Tooling:** Uses `uv` for dependency management.
*   **Linting/Formatting:** Uses `ruff` (configured in `pyproject.toml`).
*   **Typing:** Uses `pyright` in strict mode.
*   **Architecture:**
    *   `src/api/v1`: Route definitions.
    *   `src/models`: Database models (SQLModel).
    *   `src/schemas`: Pydantic schemas for request/response.
    *   `src/services`: Business logic layer.
    *   `src/core`: Configuration and security.

### Frontend (React)
*   **Structure:** Components are organized by type (`components/`, `layouts/`, `roles/`) and functionality.
*   **State/Auth:** Uses `localStorage` to store the JWT token (`usuarioLogado`).
*   **HTTP:** Axios interceptor automatically adds the `Authorization: Bearer` token to requests (except `/auth/token`).
