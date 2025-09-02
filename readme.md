# LLM Knowledge Extractor API ⚡
FastAPI-powered API for text summarization, metadata extraction, and keyword analysis

# Overview 📗
This repository contains a FastAPI-based API that ingests unstructured text, summarizes it, extracts structured metadata (title, topics, sentiment), and identifies the three most common nouns as keywords. It integrates OpenAI for LLM-powered analysis and uses PostgreSQL (via Docker) for result persistence. Documentation is auto-generated at:

Swagger: `/docs`

ReDoc: `/redoc`

# Data 🗂️
PostgreSQL is used locally via Docker. Configure DB settings through env vars:
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`

# Product 📦
API endpoints (example):
- `POST /analyze – Accepts raw text, returns summary, metadata, and extracted keywords`

# Implementation ⚙️
Tech stack:

FastAPI for API endpoints

SQLAlchemy for ORM

spaCy for keyword (noun) extraction

OpenAI API for summarization & metadata extraction

Docker & Docker Compose for local development

Design Choices:
The project is structured for modularity and maintainability. Each responsibility (LLM analysis, keyword extraction, database operations) is isolated in its own module (llm.py, nlp.py, crud.py), making it easy to extend or swap components. PostgreSQL was chosen for reliable JSON field support and easy integration with Docker. FastAPI was selected for its lightweight, async-friendly nature and built-in interactive documentation, allowing rapid prototyping without sacrificing clarity.

## Project Setup 
```bash
# 1. Clone repository
git clone https://github.com/your-repo/llm-knowledge-extractor.git
cd llm-knowledge-extractor

# 2. Create a .env file in the root directory
cat <<EOT >> .env
POSTGRES_DB=<postgresdb>
POSTGRES_USER=<postgresuser>
POSTGRES_PASSWORD=<postgrespass>
DATABASE_URL=postgresql://<POSTGRES_USER>:<POSTGRES_PASS>@db:5432/<POSTGRES_DB>
OPENAI_API_KEY=sk-xxxx
PGADMIN_DEFAULT_EMAIL=<pgadminemail>
PGADMIN_DEFAULT_PASSWORD=<pgadminpass>
EOT

# 3. Build & run with Docker Compose
docker compose up --build

```