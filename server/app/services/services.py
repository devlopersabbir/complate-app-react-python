from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(plainPassword: str, hashedPassword: str) -> bool:
    isMatch = password_context.verify(plainPassword, hashedPassword)
    if isMatch:
        return True
    else:
        return False
