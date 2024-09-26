from sqlmodel import SQLModel, create_engine, Session


class DBConfig:
    ENGINE = create_engine("sqlite:///database.db")
    SESSION = Session(bind=ENGINE)

    @classmethod
    def up(cls):
        SQLModel.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        SQLModel.metadata.drop_all(cls.ENGINE)
