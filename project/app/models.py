from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str
    email: str
    user_name: str

class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass