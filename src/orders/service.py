from sqlalchemy.orm import Session

from src.accounts.models import UserModel
from src.orders.enums import OrderStatusEnum
from src.orders.models import OrderModel
from src.orders.repository import OrderRepository
from src.orders.schemas import OrderInSchema


class OrderService:

    def __init__(self, session: Session):
        self._repository = OrderRepository(session)

    def create(self, db_user: UserModel, order: OrderInSchema) -> OrderModel:
        return self._repository.create(db_user, order)

    def get_all(self, skip: int = 0, limit: int = 100) -> list[OrderModel]:
        return self._repository.get_all(skip, limit)

    def get_by_id(self, order_id: int) -> OrderModel:
        return self._repository.get_by_id(order_id)

    def get_by_user(self, db_user: UserModel, skip: int = 0, limit: int = 100) -> list[OrderModel]:
        return self._repository.get_by_user(db_user, skip, limit)

    def update_status(self, db_order: OrderModel, status: OrderStatusEnum) -> OrderModel:
        return self._repository.update_status(db_order, status)
