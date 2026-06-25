# AI Job Application Tracker

![System Architecture](Architecture_aianalyzer.png)

AI-powered backend application that helps users manage job applications and analyze job descriptions using Large Language Models (LLMs). Built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Groq's Llama 3.1 model.

## Features

* User Registration and Login with JWT Authentication
* Secure REST APIs with Protected Endpoints
* Job Application Tracking and Management
* AI-Powered Job Description Analysis
* Extraction of Required Skills, Experience Level, Responsibilities, and Salary Insights
* PostgreSQL Database Integration
* SQLAlchemy ORM for Database Operations
* Database Versioning with Alembic Migrations
* Rate Limiting using SlowAPI
* Dockerized Application Setup
* Automated Testing with Pytest
* Clean Layered Architecture (Routes, Services, Models, Schemas)
* React Frontend Integration Planned

## System Architecture

The application follows a layered architecture:

* Client Layer (React Frontend, Swagger UI, Postman)
* FastAPI API Layer
* Authentication & Dependency Layer
* Business Logic Service Layer
* PostgreSQL Persistence Layer
* Groq AI Integration Layer
* Dockerized Deployment Layer

## Tech Stack

| Layer            | Technology          |
| ---------------- | ------------------- |
| Backend          | FastAPI             |
| Database         | PostgreSQL          |
| ORM              | SQLAlchemy          |
| Authentication   | JWT (HTTPBearer)    |
| AI Model         | Groq (Llama 3.1 8B) |
| Migrations       | Alembic             |
| Rate Limiting    | SlowAPI             |
| Testing          | Pytest              |
| Containerization | Docker              |
| Deployment       | Railway             |

## Project Structure

```text
ai_analyzer/
│
├── app/
│   ├── core/
│   ├── dependencies/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── migrations/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
└── README.md
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Farru049/ai_analyzer.git
cd ai_analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux / macOS:

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create PostgreSQL Database

```text
analyzer_db
```

### 6. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/analyzer_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

GROQ_API_KEY=your_groq_api_key
```

### 7. Run Database Migrations

```bash
alembic upgrade head
```

### 8. Start the Application

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Running with Docker

Build and run:

```bash
docker-compose up --build
```

## Running Tests

```bash
pytest
```

## API Endpoints

### Authentication

| Method | Endpoint  | Description   |
| ------ | --------- | ------------- |
| POST   | /register | Register User |
| POST   | /login    | Login User    |

### Applications

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | /applications      | Get All Applications |
| POST   | /applications      | Create Application   |
| GET    | /applications/{id} | Get Application      |
| PUT    | /applications/{id} | Update Application   |
| DELETE | /applications/{id} | Delete Application   |

### AI

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| POST   | /ai/analyze | Analyze Job Description |

## AI Analysis Workflow

1. User submits a job description.
2. FastAPI validates and authenticates the request.
3. AI Service constructs a prompt.
4. Prompt is sent to Groq's Llama 3.1 model.
5. AI-generated insights are returned.
6. Analysis can be stored alongside the application record.

## Database Schema

### Users

* id
* email
* hashed_password
* created_at

### Applications

* id
* user_id
* company_name
* role
* status
* description
* analysis
* notes
* applied_at

Relationship:

```text
User (1) ------ (N) Applications
```

## Deployment

* Dockerized Application
* Railway Deployment
* PostgreSQL Database
* Groq Cloud AI Service

## Future Enhancements

* React Frontend Integration
* Redis Caching
* Token Blacklisting with Redis
* Async SQLAlchemy
* CI/CD using GitHub Actions
* Prometheus Monitoring
* Role-Based Access Control (RBAC)

## Author

**Mohammad Farhaan Ali**

GitHub: https://github.com/Farru049
