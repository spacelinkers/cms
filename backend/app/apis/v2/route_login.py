from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from jose import jwt, JWTError

from app.db.session import get_db
from app.db.repository.login import get_user
from app.core.security import create_access_token
from app.core.hashUtil import HashUtil
from app.core.config import settings
from app.apis.v2.utils import OAuth2PasswordBearerWithCookie

router = APIRouter()


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)

    if not user:
        return False
    if not HashUtil.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token")
def login_for_access_token(
        response: Response,
        form_data: OAuth2PasswordRequestForm=Depends(),
        db: Session = Depends(get_db)
    ):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(
        data = {"sub": user.email},
        expires_delta = access_token_expires
    )

    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")

def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        print("email is",username)
        if username is None:
            raise credentials_exception
    except JWTError:
        print("2")
        raise credentials_exception
    user = get_user(username=username, db=db)
    print(user)
    print("3")
    if user is None:
        print("4")
        raise credentials_exception
    return user