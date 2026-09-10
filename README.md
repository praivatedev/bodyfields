# FastAPI – Body Fields

A minimal example demonstrating how to declare and validate request body fields in FastAPI using Pydantic.

## Concepts Covered

| Concept | Where it's shown |
|---------|-----------------|
| Optional fields (`str \| None`) | `description`, `tax` |
| Field constraints (`gt`, `max_length`) | `price` (must be > 0), `description` (max 3000 chars) |
| Field metadata (`title`, `description`) | Shown in Swagger docs |
| Embedded body (`embed=True`) | Wraps the model in an `"item"` key |

## Setup

```bash
uv init
uv add fastapi uvicorn
uv run uvicorn main:app --reload   