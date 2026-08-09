from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITH = settings.ALGORITH
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# TOken Create
def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITH)

def validate_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITH)
        return payload
    except JWTError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Token"
        )