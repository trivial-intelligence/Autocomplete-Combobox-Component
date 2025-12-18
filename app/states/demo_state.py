import reflex as rx
from app.states.autocomplete_state import AutocompleteItem

FRAMEWORKS: list[AutocompleteItem] = [
    {
        "name": "React",
        "value": "react",
        "keywords": ["web", "frontend", "js", "library"],
    },
    {
        "name": "Vue.js",
        "value": "vue",
        "keywords": ["web", "frontend", "js", "framework"],
    },
    {
        "name": "Angular",
        "value": "angular",
        "keywords": ["web", "frontend", "ts", "framework"],
    },
    {"name": "Svelte", "value": "svelte", "keywords": ["web", "frontend", "compiler"]},
    {
        "name": "Next.js",
        "value": "nextjs",
        "keywords": ["web", "react", "backend", "fullstack"],
    },
    {
        "name": "Python",
        "value": "python",
        "keywords": ["backend", "scripting", "ai", "data"],
    },
    {
        "name": "Reflex",
        "value": "reflex",
        "keywords": ["python", "web", "fullstack", "ui"],
    },
    {
        "name": "Django",
        "value": "django",
        "keywords": ["python", "backend", "web", "framework"],
    },
    {
        "name": "FastAPI",
        "value": "fastapi",
        "keywords": ["python", "backend", "api", "async"],
    },
    {
        "name": "Tailwind CSS",
        "value": "tailwind",
        "keywords": ["css", "styling", "utility"],
    },
    {
        "name": "TypeScript",
        "value": "typescript",
        "keywords": ["js", "types", "microsoft"],
    },
    {
        "name": "Docker",
        "value": "docker",
        "keywords": ["ops", "containers", "deployment"],
    },
    {
        "name": "Kubernetes",
        "value": "k8s",
        "keywords": ["ops", "orchestration", "cloud"],
    },
    {"name": "PostgreSQL", "value": "postgres", "keywords": ["db", "sql", "database"]},
    {"name": "Redis", "value": "redis", "keywords": ["db", "cache", "kv"]},
]