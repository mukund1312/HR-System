# from fastapi import Depends, HTTPException
# from app.auth.dependencies import get_current_user
# # from app.users.schemas import User
# from app.db.models.user import User
# from fastapi.security import OAuth2PasswordBearer
# # from fastapi.security import OAuth2PasswordBearer

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login-test")

# def require_permission(permission: str):
#     def checker(user: User = Depends(get_current_user)):
#         if permission not in user.permissions:
#             raise HTTPException(
#                 status_code=403,
#                 detail="Permission denied"
#             )
#         return user  # 👈 SQLAlchemy User
#     return checker




# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db),
# ):
#     payload = decode_token(token)
#     user = db.query(User).filter(User.id == payload["sub"]).first()

#     if not user:
#         raise HTTPException(status_code=401)

#     return user


# app/core/dependencies.py
from fastapi import Depends, HTTPException
from app.auth.dependencies import get_current_user
from app.db.models.user import User

def require_permission(permission: str):
    def checker(user: User = Depends(get_current_user)):
        if permission not in user.permissions:
            raise HTTPException(status_code=403, detail="Permission denied")
        return user
    return checker
