# app/auth/dependencies.py
# from fastapi.security import OAuth2PasswordBearer

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="/auth/login-test"
# )
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

# from fastapi import Depends, HTTPException
# # from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# # from app.db.dependencies import get_db
# from app.db.dependencies import get_db
# from app.db.models.user import User
# from app.auth.utils import decode_token

# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login-test")

# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db),
# ):
#     payload = decode_token(token)
#     user = db.query(User).filter(User.id == payload["sub"]).first()

#     if not user:
#         raise HTTPException(status_code=401)

#     return user
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from types import SimpleNamespace
from app.auth.utils import decode_token

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    payload = decode_token(token)

    # 🚨 NO DATABASE LOOKUP HERE
    return SimpleNamespace(
        id=payload["sub"],
        email=payload["email"],
        role=payload["role"],
        permissions=payload["permissions"],
    )

