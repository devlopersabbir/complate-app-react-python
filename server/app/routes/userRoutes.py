from fastapi import APIRouter
from app.models.userModel import User


router = APIRouter()

# @router.post("/users", response_model=User)
# async def createUser(user: UserCreate, db: Session = Depend())
