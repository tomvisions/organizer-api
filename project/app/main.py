from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session, init_db
from app.models import User, UserCreate

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/user", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    
    return [User(name=user.name, user_name=user.user_name, email=user.email, id=user.id) for user in users]


@app.post("/user")
async def add_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(name=user.name, user_name=user.user_name, email=user.email)
 
    session.add(user)
    
    await session.commit()
    await session.refresh(user)
    
    return user

@app.put("/user")
async def add_user(user: User, session: AsyncSession = Depends(get_session)):
    user = User(name=user.name, user_name=user.user_name, email=user.email)
    session.add(user)
    
    await session.commit()
    await session.refresh(user)
    
    return user
