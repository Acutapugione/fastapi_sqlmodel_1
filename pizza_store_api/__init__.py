from fastapi import FastAPI, APIRouter
from uvicorn import run as asgi_run
from .db import DBConfig, Product

app = FastAPI(debug=True)

from . import pizza


def migrate():
    DBConfig.SESSION.bulk_save_objects(
        [
            Product(
                name=f"Pizza_{x}",
                description="fresh meat pizza",
                price=150,
            )
            for x in range(10)
        ]
    )
    DBConfig.SESSION.commit()


def main():
    DBConfig.down()
    DBConfig.up()
    migrate()
    asgi_run(app)


if __name__ == "__main__":
    main()
