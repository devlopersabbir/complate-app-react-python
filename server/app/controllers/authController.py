from sqlalchemy.orm import Session
from fastapi import status
from fastapi.responses import JSONResponse
from app.schemas.userSchema import UserLoginSchema
from app.libs.reuses import find_by_username
from app.models.userModel import User
from fastapi.security import OAuth2PasswordBearer
from app.services.services import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def auth_login(req_data: UserLoginSchema, db: Session):
    if not req_data.username or not req_data.password:
        return JSONResponse(
            content={
                "message": "Please fill required field!"
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )
    # check our user have on db or not using username
    isUser = find_by_username(db, User, req_data.username)
    if not isUser:
        return JSONResponse(
            content={
                "message": "User not found!"
            },
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    # verify password
    isValid = verify_password(req_data.password, isUser.password)

    if not isValid:
        return JSONResponse(
            content={
                "message": "Invalid password!"
            },
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    return {
        "mess": "works"
    }
