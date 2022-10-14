import logging

from sqlalchemy import select

from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import Session

from ..abstract_repo import AbstractRepository
from .dto import User
from .models import SQLA_User


class Repository(AbstractRepository):
    def __init__(self, session):
        self.session: Session = session

        self.logger = logging.getLogger(__name__)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )

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
            self.logger.error('Multiple users with same id!')

        return False

    def commit_pending(self,):
        self.session.commit()
