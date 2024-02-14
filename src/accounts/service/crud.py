from sqlalchemy import select
from sqlalchemy.orm import Session

from src.accounts.models import User
from src.accounts.schemas import UserCreate
from src.accounts.utils.auth import get_password_hash


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # return db.query(User).offset(skip).limit(limit).all()

    stmt = select(User).offset(skip).limit(limit)

    return db.scalars(stmt).all()
