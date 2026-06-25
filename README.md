# AI Job Application Tracker

A full-stack application that helps you track job applications and get AI-powered analysis of job descriptions.

## Tech Stack

- **Backend:** FastAPI, PostgreSQL, SQLAlchemy
- **AI:** Groq (Llama 3.1 8B)
- **Authentication:** JWT with HTTPBearer
- **Testing:** pytest with isolated fixtures
- **Containerization:** Docker

## Features

- User registration and login with JWT tokens
- Track job applications with company, role, and job description
- AI analysis of job descriptions using Groq
- Extracts required skills, experience level, responsibilities, salary
- Secure endpoints with authentication
- Full test coverage for auth endpoints
-FReact Frontend has to be integrated(not yet done)

## Setup

### Local Development

1. Clone repo
2. Create virtual environment: `python -m venv myenv`
3. Activate: `myenv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`
5. Create PostgreSQL database: `analyzer_db`
6. Create `.env` file with: