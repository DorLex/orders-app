from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.accounts.models import User
from src.accounts.service.auth import get_current_user, verify_token
from src.dependencies import get_db
from src.orders.schemas import OrderIn, OrderOut
from src.orders.service.crud import create_order, get_orders, get_user_orders

router = APIRouter(
    prefix='/orders',
    tags=['orders'],
    dependencies=[Depends(verify_token)]
)


@router.get('/', response_model=list[OrderOut])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = get_orders(db, skip=skip, limit=limit)
    return orders


@router.post('/')
async def add_order(
        order: OrderIn,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
) -> OrderOut:
    return create_order(db, current_user.id, order)


@router.get('/my/', response_model=list[OrderOut])
def read_my_orders(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user_orders = get_user_orders(db, current_user, skip=skip, limit=limit)
    return user_orders
