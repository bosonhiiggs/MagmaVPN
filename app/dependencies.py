from typing import Annotated
import jwt
from fastapi import Depends, HTTPException
from jwt import InvalidTokenError
from starlette import status

from .config.config import ALGORITHM, SECRET_KEY
from .schemas.user import User, TokenData
from fastapi.security import OAuth2PasswordBearer
from .utils import get_user_data

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
jwt_secret_key = SECRET_KEY
jwt_algorithms = ALGORITHM


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=jwt_algorithms)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

    except InvalidTokenError:
        raise credentials_exception
    user_data = get_user_data(token_data.username)
    if user_data is None:
        raise credentials_exception
    return user_data
