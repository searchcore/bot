from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    nickname: str
    lang: str

    class Config:
        orm_mode = True
