

```text
my-project/
├── pyproject.toml
├── poetry.lock
├── README.md
├── .python-version
├── .gitignore
├── .env
│
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── config/
│       │   ├── settings.py
│       │   └── logging.py
│       │
│       ├── api/
│       │   ├── routes/
│       │   ├── dependencies/
│       │   └── middleware/
│       │
│       ├── core/
│       │   ├── exceptions.py
│       │   ├── security.py
│       │   └── constants.py
│       │
│       ├── services/
│       │   ├── user_service.py
│       │   └── payment_service.py
│       │
│       ├── models/
│       │   └── user.py
│       │
│       ├── repositories/
│       │   └── user_repo.py
│       │
│       ├── utils/
│       │   └── helpers.py
│       │
│       └── db/
│           ├── session.py
│           └── migrations/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── scripts/
│   ├── seed_db.py
│   └── dev_server.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── docs/
    └── architecture.md
```