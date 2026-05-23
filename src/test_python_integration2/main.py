import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class AppConfig:
    db_url: str
    secret_key: str
    debug: bool


def load_app_config() -> AppConfig:
    return AppConfig(
        db_url=os.getenv("DATABASE_URL", "changeme"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
        secret_key=os.getenv("SECRET_KEY", "changeme"),
    )


app_config = load_app_config()

print(f"App config is: {app_config}")
