from sqlalchemy import select
from sqlalchemy.orm import Session

from src.orders.models import Order
from src.orders.schemas import OrderIn


def create_order(db: Session, order: OrderIn):
    db_order = Order(
        title=order.title,
        status=order.status
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(Order).offset(skip).limit(limit)
    return db.scalars(stmt).all()
