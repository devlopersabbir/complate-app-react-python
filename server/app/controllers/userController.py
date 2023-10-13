from app.models.userModel import User


async def createUser(db: Session, userData: dict):
    user = User(**userData)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
