from sqlalchemy import (
    Column,
    BigInteger,
    String,
)

from ..database import Base

class SQLA_User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    lang = Column(String, nullable=False)