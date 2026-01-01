from fastapi import FastAPI, Depends
from app.auth.routes import router as auth_router
from app.core.dependencies import require_permission
from app.core.permissions import CANDIDATE_READ
from app.users.schemas import User
from app.hiring.candidates.routes import router as candidate_router



app = FastAPI(title="Interview Platform API")
app.include_router(auth_router)
app.include_router(candidate_router)
@app.get("/candidates")
def get_candidates(
    user: User = Depends(require_permission(CANDIDATE_READ))
):
    return {
        "message": "Candidates visible",
        "user": user.email
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
