from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.configs.database import get_db
from app.schemas.userSchema import UserLoginSchema
from app.controllers.authController import auth_login

router = APIRouter()


@router.post("/login", tags=["Login"])
async def login(req_data: UserLoginSchema, db: Session = Depends(get_db)):
    try:
        return await auth_login(req_data, db)
    except Exception as err:
        return JSONResponse(
            content={
                "message": "Something went wrong!",
                "error": str(err)
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
