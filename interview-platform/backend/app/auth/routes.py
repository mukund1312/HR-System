# from fastapi import APIRouter
# from app.core.security import create_access_token
# from app.core.rbac import ROLE_PERMISSIONS

# router = APIRouter(prefix="/auth", tags=["auth"])

# # @router.post("/login-test")
# # def login_test():
# #     role = "interviewer"

# #     token = create_access_token({
# #         "sub": "user-123",
# #         "email": "test@example.com",
# #         "role": role,  # 👈 SINGLE role
# #         "permissions": list(ROLE_PERMISSIONS[role])
# #     })

# #     return {
# #         "access_token": token,
# #         "token_type": "bearer"
# #     }

# from uuid import UUID
# from fastapi import APIRouter
# from app.core.security import create_access_token
# from app.core.rbac import ROLE_PERMISSIONS

# # router = APIRouter(prefix="/auth", tags=["auth"])

# # @router.post("/login-test")
# # def login_test():
# #     role = "interviewer"

# #     user_id = "a3c9e3f4-9a5e-4b7b-9d6c-1e8e7b1a1234"  # 👈 REAL UUID

# #     token = create_access_token({
# #         "sub": user_id,              # ✅ UUID string
# #         "email": "test@example.com",
# #         "role": role,
# #         "permissions": list(ROLE_PERMISSIONS[role])
# #     })

# #     return {
# #         "access_token": token,
# #         "token_type": "bearer"
# #     }
# from fastapi import Depends
# from sqlalchemy.orm import Session
# from app.db.dependencies import get_db

# from uuid import uuid4
# from app.db.models.user import User
# from app.db.dependencies import get_db
# from fastapi import APIRouter, Depends

# @router.post("/login-test")
# def login_test(db: Session = Depends(get_db)):
#     role = "interviewer"
#     user_id = uuid4()

#     # ✅ CREATE USER IF NOT EXISTS
#     user = User(
#         id=user_id,
#         email="test@example.com",
#         name="Test User",
#         role=role,
#     )
#     db.add(user)
#     db.commit()

#     token = create_access_token({
#         "sub": str(user_id),   # 👈 REAL UUID
#         "email": user.email,
#         "role": role,
#         "permissions": list(ROLE_PERMISSIONS[role]),
#     })

#     return {"access_token": token, "token_type": "bearer"}


import uuid
from fastapi import APIRouter
# Import these from your existing project structure
from app.core.security import create_access_token
from app.core.rbac import ROLE_PERMISSIONS

# Initialize the router
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login-test")
def login_test():
    # You can change this string to "admin" or "recruiter" to test different roles
    role = "interviewer"
    
    # 1️⃣ Generate a proper UUID string so PostgreSQL doesn't crash
    test_user_id = str(uuid.uuid4()) 

    # 2️⃣ Create the token using your core security function
    token = create_access_token({
        "sub": test_user_id,          
        "email": "test@example.com",
        "role": role,
        "permissions": list(ROLE_PERMISSIONS[role]),
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "debug_info": {
            "user_id": test_user_id,
            "role": role
        }
    }