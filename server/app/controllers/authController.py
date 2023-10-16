from sqlalchemy.orm import Session
from fastapi import status
from fastapi.responses import JSONResponse
from app.schemas.userSchema import UserLoginSchema
from app.libs.reuses import find_by_username
from app.models.userModel import User


async def auth_login(req_data: UserLoginSchema, db: Session):
    print(req_data.username)
    print(req_data.password)
    if not req_data.username or not req_data.password:
        return JSONResponse(
            content={
                "message": "Please fill required field!"
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )

    isUser = find_by_username(db, User, req_data.username)
    print(isUser)
    return
