from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str
    email: str
    user_name: str

class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass

class EventBase(SQLModel):
    name: str
    description: str

class Event(EventBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class EventCreate(EventBase):
    pass