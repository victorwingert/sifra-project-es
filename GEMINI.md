# SIFRA Project Context

## Project Overview
SIFRA (Sistema Integrado de Frequência e Assiduidade) is a full-stack application designed for managing school attendance.
The project currently supports a **React** frontend and contains two distinct backend implementations:
1.  **Java (Spring Boot):** The primary, active backend implementation.
2.  **Python (FastAPI):** A modern, likely experimental or in-progress backend implementation.

## 📂 Directory Structure

| Directory | Description | Technology |
| :--- | :--- | :--- |
| `frontend/` | The web user interface. | React (Create React App), Axios |
| `backend/` | The main application server. | Java 21, Spring Boot 3.5.4, Maven |
| `backend-python/` | Alternative/New application server. | Python 3.13, FastAPI, SQLModel, UV |

---

## 🚀 Getting Started

### 1. Frontend (React)
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
*   **Configuration:**
    *   API Base URL is set in `src/service/api.js`. Currently points to `http://localhost:8080` (Java Backend).

### 2. Backend (Java Spring Boot)
*   **Directory:** `backend/`
*   **Prerequisites:** Java JDK 21
*   **Installation:** Uses Maven Wrapper (`mvnw`), no manual install needed.
*   **Running:**
    ```bash
    cd backend
    ./mvnw spring-boot:run
    ```
    *   Server runs on: `http://localhost:8080`
*   **Configuration:**
    *   Main config file: `src/main/resources/application.properties`.
    *   **Database:** Currently configured to connect to a remote PostgreSQL instance on Render.

### 3. Backend (Python FastAPI)
*   **Directory:** `backend-python/`
*   **Prerequisites:** Python 3.13+, `uv` (project manager).
*   **Installation:**
    ```bash
    cd backend-python
    uv sync
    ```
*   **Running:**
    ```bash
    uv run fastapi dev src/main.py
    ```
*   **Key Tech:** Uses `sqlmodel` for ORM, `pydantic-settings` for config, and `ruff`/`pyright` for linting/typing.

---

## 🛠 Development Conventions

### Code Style
*   **Java:** Standard Spring Boot layered architecture (`Controller` -> `Service` -> `Repository` -> `Model`). Uses Lombok for boilerplate reduction.
*   **Python:** Modern async FastAPI. Strict typing enforced by `pyright`.
*   **Frontend:** Functional React components with Hooks. CSS modules/stylesheets per component.

### Key Configuration Files
*   `frontend/src/service/api.js`: Handles API connections. Modify this if switching between Java and Python backends (ports 8080 vs 8000).
*   `backend/src/main/resources/application.properties`: Java DB and Server config.
*   `backend-python/pyproject.toml`: Python dependencies and tool settings.

### Database
*   The project uses **PostgreSQL**.
*   The Java backend is pre-configured with credentials for a remote development database.
