# FastAPI Blog API

A RESTful blog API built with FastAPI, SQLAlchemy, and JWT authentication.

## Tech Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL (via psycopg2)
- **Auth:** JWT (python-jose)
- **Validation:** Pydantic v2
- **Server:** Uvicorn

## Project Structure

```
.
├── main.py          # App entry point, route definitions
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic request/response schemas
├── auth.py          # JWT token creation and validation
├── database.py      # DB engine and session setup
├── config.py        # Environment variable settings
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd FastAPI-blog-api-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/blogdb
SECRET_KEY=your_secret_key
ALOGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

## API Endpoints

### Auth

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/login` | No | Get a JWT access token |

### Blogs

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/` | No | Health check |
| GET | `/blogs` | No | List blogs (paginated, searchable) |
| GET | `/blogs/{id}` | No | Get a blog by ID |
| POST | `/blogs` | Yes | Create a blog |
| PUT | `/blogs/{id}` | Yes | Update a blog |
| DELETE | `/blogs/{id}` | Yes | Delete a blog |

### Query Parameters — `GET /blogs`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `limit` | int | 5 | Results per page |
| `search` | string | `""` | Filter by title (case-insensitive) |

## Authentication

Protected endpoints require a Bearer token in the `Authorization` header.

**Get a token:**
```bash
curl -X POST http://localhost:8000/login
```

**Use the token:**
```bash
curl -H "Authorization: Bearer <token>" http://localhost:8000/blogs
```

## Database Model

**Blog**

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key |
| `title` | String | Blog title |
| `content` | Text | Blog content |
