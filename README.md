# 🎯 AI Skill Gap Analyzer

 **Upload a resume. Paste a job description. Know exactly what to learn next.**

An AI-powered career intelligence platform that compares a candidate's resume against a target job, finds the skill gaps, calculates an **explainable** match score, and builds a personalized learning roadmap, project ideas, and interview practice.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-orange)

---

## 🤔 The Problem

Students and freshers apply to dozens of jobs without knowing:

- What skills do I already have?
- What does this job actually require?
- What am I missing, and what should I learn **first**?
- Why is my resume getting rejected?

Most resume tools give a vague score. This project gives **answers you can act on**.

## ✨ What It Does

| Feature | Description |
|---|---|
| 📄 **Resume parsing** | Reads PDF, DOCX, and TXT resumes |
| 🧾 **Job description parsing** | Extracts required skills from any pasted JD |
| 🧠 **Semantic skill matching** | Understands that "ML" ≈ "Machine Learning" using embeddings, not just keywords |
| 📊 **Explainable match score** | Shows *why* the score is what it is, skill by skill |
| 🟢🟡🔴 **Gap analysis** | Splits skills into strong, partial, and missing |
| 🗺️ **Learning roadmap** | AI-generated, prioritized plan for closing the gaps |
| 🛠️ **Project recommendations** | Portfolio projects that target your missing skills |
| 🎤 **Interview practice** | Role-specific questions, mock interviews, and AI feedback |
| 💬 **AI career assistant** | RAG-powered chat over a career/learning knowledge base |
| 📈 **Progress tracking** | History of past analyses and improvement over time |
| 📑 **Report export** | Download a final career-gap report |

## 🏗️ Architecture

```mermaid
flowchart TD
    U[User] --> F[Frontend: HTML / CSS / JS]
    F --> API[FastAPI]
    API --> AUTH[JWT Authentication]
    AUTH --> SVC[Application Services]
    SVC --> NLP[NLP: parsing, skill extraction, normalization]
    SVC --> MATCH[Semantic Matching + Gap Analysis]
    SVC --> RAG[RAG Engine]
    MATCH --> LLM[LLM / Embedding Provider]
    RAG --> LLM
    RAG --> VDB[(Vector Search)]
    SVC --> DB[(Database)]
```

**Design principles**

- **Layered:** API routes stay thin, logic lives in `services/`, AI code lives in `ai/`.
- **Provider-agnostic LLM layer:** swap OpenAI-compatible providers without touching business logic.
- **Explainable first:** the match score comes from transparent rules and embeddings, not a black-box prompt. The LLM is used for *explaining and recommending*, not for inventing the score.
- **Config via environment variables:** no secrets in code.

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Backend | Python 3.12+, FastAPI, Pydantic, SQLAlchemy, Alembic |
| Database | SQLite (development) → PostgreSQL + pgvector (production) |
| NLP / ML | spaCy, sentence-transformers, scikit-learn |
| Documents | PyMuPDF, python-docx |
| Auth | JWT, bcrypt password hashing |
| LLM | Provider abstraction (OpenAI-compatible) |
| Frontend | HTML, CSS, JavaScript (React-migration friendly) |
| DevOps | Docker, Docker Compose |
| Testing | pytest, httpx |

## 🚦 Project Status

- [x] **Phase 0:** Project setup, config, FastAPI skeleton
- [x] **Phase 1:** Users, JWT authentication (register / login / me)
- [ ] **Phase 2:** Resume upload and text extraction (PDF, DOCX, TXT)
- [ ] **Phase 3:** Skill extraction and normalization
- [ ] **Phase 4:** Job description parsing and semantic matching
- [ ] **Phase 5:** Gap analysis and explainable match score
- [ ] **Phase 6:** LLM client, roadmap, project and interview generation
- [ ] **Phase 7:** RAG with vector search and career chat
- [ ] **Phase 8:** Frontend dashboard and report export
- [ ] **Phase 9:** Tests, logging, Docker, deployment

## 📁 Project Structure

```
ai-skill-gap-analyzer/
├── app/
│   ├── main.py
│   ├── api/          # Route handlers (auth, resume, jobs, analysis, ...)
│   ├── core/         # Config, security, logging, exceptions
│   ├── db/           # Engine, session, models, migrations
│   ├── schemas/      # Pydantic request/response models
│   ├── services/     # Parsing, matching, gap analysis, roadmap, ...
│   ├── ai/           # LLM client, embeddings, prompts, RAG, agents
│   ├── utils/        # File and text helpers
│   └── tests/
├── frontend/         # HTML / CSS / JS dashboard
├── data/             # Knowledge base and sample resumes
├── scripts/          # Seeding and document ingestion
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## 🚀 Getting Started (Windows / PowerShell)

**Prerequisites:** Python 3.12+, Git, VS Code (optional)

```powershell
# 1. Clone
git clone https://github.com/<your-username>/ai-skill-gap-analyzer.git
cd ai-skill-gap-analyzer

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env

# 5. Run the app
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000/docs** for the interactive API documentation.

### Environment variables

```env
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=change-me
ACCESS_TOKEN_EXPIRE_MINUTES=60
LLM_API_KEY=
LLM_MODEL=
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

> For PostgreSQL, change `DATABASE_URL` to
> `postgresql+psycopg://user:password@localhost:5432/dbname`
> and run `docker compose up -d db` to start the pgvector database.

## 🔌 API Overview

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | `/health` | Health check | ✅ |
| POST | `/auth/register` | Create an account | ✅ |
| POST | `/auth/login` | Get a JWT access token | ✅ |
| GET | `/auth/me` | Current user profile | ✅ |
| POST | `/resume/upload` | Upload and parse a resume | 🔜 |
| POST | `/jobs` | Save a job description | 🔜 |
| POST | `/analysis` | Run a skill gap analysis | 🔜 |
| GET | `/roadmap/{id}` | Personalized learning roadmap | 🔜 |
| POST | `/interview/start` | Start a mock interview | 🔜 |
| POST | `/chat` | Ask the AI career assistant | 🔜 |
| GET | `/reports/{id}` | Export a career-gap report | 🔜 |

## 🧮 How the Match Score Works *(planned design)*

1. Extract skills from the resume and from the job description.
2. Normalize them (`"py"`, `"python3"` → `Python`).
3. Compare using embeddings so related skills get **partial** credit.
4. Weight each required skill by importance (must-have vs nice-to-have).
5. Return a score **with a breakdown**: which skills matched, which partially matched, and which are missing.

## 🔐 Security Notes

- Passwords are hashed with bcrypt, never stored in plain text.
- JWT tokens expire and are verified on every protected route.
- Secrets live in `.env`, which is git-ignored.
- Change `SECRET_KEY` to a long random value before any real deployment.

## 🗺️ Roadmap Beyond v1

- OCR for scanned resumes
- React frontend
- Resume rewriting suggestions
- Multi-language support
- Cloud deployment guide

## 🤝 Contributing

Ideas and pull requests are welcome. Open an issue first to discuss larger changes.

## 📄 License

MIT License. See `LICENSE` for details.
