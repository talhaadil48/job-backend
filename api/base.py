from fastapi import APIRouter

class BaseRouter:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):
        return self.router
