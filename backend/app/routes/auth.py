from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.schemas.auth import TokenResponse
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(body: UserCreate, db: AsyncSession = Depends(get_db)):
    
    existing_username = await db.exec(select(User).where(User.username == body.username))
    if existing_username.first():
        raise HTTPException(status_code=400, detail="Username already taken")

    existing_email = await db.exec(select(User).where(User.email == body.email))
    if existing_email.first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=body.username,
        email=body.email,
        hashed_password=hash_password(body.password),
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return TokenResponse(access_token=create_access_token(new_user.id))


@router.post("/login", response_model=TokenResponse)
async def login(body: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.exec(select(User).where(User.email == body.email))
    user = result.first()

    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return TokenResponse(access_token=create_access_token(user.id))
