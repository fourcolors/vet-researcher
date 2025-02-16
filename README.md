# Vet Researcher

An AI-powered tool for researching and analyzing veterinary medical histories.

## Prerequisites

- [mise](https://mise.jdx.dev/) for Python version management
- [Poetry](https://python-poetry.org/) for dependency management

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd vet-researcher
```

2. Install Python and Poetry with mise:

```bash
mise install
```

3. Install dependencies:

```bash
poetry install
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### CLI Tool

Run analysis via command line:

```bash
# Basic analysis
poetry run vet-researcher analyze "My dog has been limping for 2 days"

# Save output to file
poetry run vet-researcher analyze "My dog has been limping for 2 days" -o results.txt
```

### API Server

1. Start the API server:

```bash
poetry run vet-researcher-api
```

2. The API will be available at `http://localhost:8000`

3. API Endpoints:
   - POST `/analyze`: Analyze a veterinary case
   - GET `/docs`: Interactive API documentation (Swagger UI)
   - GET `/redoc`: Alternative API documentation

Example API request:

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"query": "My 5-year-old golden retriever has been limping"}'
```

## Development

- Format code:

```bash
poetry run black .
poetry run isort .
```

- Run tests:

```bash
poetry run pytest
```

## Project Structure

```
vet_researcher/
├── api/            # API endpoints
│   ├── models.py   # API data models
│   └── main.py     # FastAPI application
├── core/           # Core functionality
├── utils/          # Utility functions
└── cli/            # Command-line interface

tests/              # Test files
```

## License

MIT
