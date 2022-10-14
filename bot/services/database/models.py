from sqlalchemy import (
    Column,
    BigInteger,
    String,
)

from sqlalchemy import select

from .database import Base
from .entities import UserMixin


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    lang = Column(String, nullable=False)

    @classmethod
    def create(cls, s, user):
        s.add(user)
        s.commit()

    @classmethod
    def is_exists(cls, s, user):
        stmt = select(cls).where(cls.id == user.id)

        result = s.execute(stmt).one_or_none()

        return bool(result)
