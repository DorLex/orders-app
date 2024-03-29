from fastapi import FastAPI

from src.accounts.routers import users, auth
from src.accounts.routers import registration
from src.orders.routers import orders

app = FastAPI(
    title='Orders App',
)

app.include_router(users.router)
app.include_router(orders.router)
app.include_router(registration.router)
app.include_router(auth.router)
