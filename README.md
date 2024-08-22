# FastAPI Blog API

This is a simple FastAPI blog API that includes authentication and validation.

## Features

- User registration and login
- Create, read, update, and delete posts
- JWT authentication
- SQLAlchemy ORM

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (Optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-blog-api.git
   cd fastapi-blog-api
   ```

2. installing the venv:

   ### For Unix/macOS

   ```bash
   python3 -m venv venv
   ```

   ### For Windows

   ```bash
   python -m venv venv
   ```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Set up the environment variables:

```bash
cp .env.example .env
```

5. Start the application:

```bash
uvicorn app.main:app --reload
```

### Running with Docker

1. Build the Docker image:

```bash
docker build -t fastapi-blog-api .
```

2. Run the Docker container:

```bash
docker run -p 80:80 fastapi-blog-api
```

### Running with Docker Compose

2. Run the Docker container:

```bash
docker-compose up --build
```

## Usage

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.

## Endpoints

- `/api/v1/auth/register`: Register a new user
- `/api/v1/auth/login`: Login and get a JWT token
- `/api/v1/posts/`: CRUD operations on blog posts
