import logging
from sqlalchemy import (
    Column,
    BigInteger,
    String,
)

from sqlalchemy import (
    select,
)

from sqlalchemy.exc import MultipleResultsFound

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker, Session

from .models import User

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class SQLA_User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    lang = Column(String, nullable=False)


def _configure_sqla(db_url, echo):
    engine = create_engine(db_url, echo=echo, future=True)

    session = sessionmaker(engine)

    mapper_registry.metadata.create_all(engine)

    return session


class Database():
    def __init__(self, db_url, echo=True):
        _session_factory = _configure_sqla(db_url, echo=echo)
        self.session_factory = _session_factory

    def new_session(self):
        return self.session_factory()


class Repository():
    def __init__(self, session):
        self.session: Session = session

    def create_user(self, user: User):
        _user = SQLA_User(**user.dict())

        self.session.add(_user)
        self.session.commit()

    def is_user_exists(self, user: User):
        stmt = select(SQLA_User).where(SQLA_User.id == user.id)

        try:
            result = self.session.execute(stmt).one_or_none()
            return bool(result)
        except MultipleResultsFound:
            logger.error('Multiple users with same id!')

        return False

    def commit_pending(self,):
        self.session.commit()
