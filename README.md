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
├── core/           # Core functionality
├── utils/          # Utility functions
└── cli/            # Command-line interface

tests/              # Test files
```

## License

MIT
