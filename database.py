from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from settings import settings

Tortoise.init_models(["models"], "models")

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:5432/{settings.DB_NAME}",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        modules={"models": ["models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

