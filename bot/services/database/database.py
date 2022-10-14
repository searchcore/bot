from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker, Session


mapper_registry = registry()
Base = mapper_registry.generate_base()


class Database:
    def __init__(self, db_url, echo=True):
        _sessionmaker = Database._configure_sqla(db_url, echo=echo)
        self._sessionmaker = _sessionmaker

    def new_session(self) -> Session:
        return self._sessionmaker()

    @staticmethod
    def _configure_sqla(db_url, echo) -> sessionmaker:
        engine = create_engine(db_url, echo=echo, future=True)

        _sessionmaker = sessionmaker(engine)

        mapper_registry.metadata.create_all(engine)

        return _sessionmaker
