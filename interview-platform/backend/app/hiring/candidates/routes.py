from fastapi import APIRouter, Depends, HTTPException
# from app.hiring.candidates.schemas import Candidate, StateChangeRequest
from app.hiring.candidates.schemas import StateChangeRequest
from app.db.models.candidate import Candidate

from app.hiring.candidates.state_machine import validate_transition
from app.hiring.candidates.states import CandidateState
from app.core.dependencies import require_permission
from app.core.permissions import CANDIDATE_UPDATE
from sqlalchemy.orm import Session
# from fastapi import Depends
from uuid import UUID
from app.hiring.candidates.permissions import can_user_transition
from app.core.permissions import INTERVIEW_FEEDBACK

from app.db.dependencies import get_db
from app.db.models.candidate import Candidate
from app.db.models.candidate_state_history import CandidateStateHistory
from app.hiring.candidates.states import CandidateState

router = APIRouter(prefix="/candidates", tags=["candidates"])

# TEMP in-memory candidate (DB later)
# FAKE_CANDIDATE = {
#     "id": "cand-1",
#     "name": "John Doe",
#     "email": "john@example.com",
#     "current_state": CandidateState.APPLIED
# }

@router.get("/{candidate_id}")
def get_candidate(candidate_id: UUID, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate

# @router.post("/{candidate_id}/transition")
# def change_state(
#     candidate_id: UUID,
#     data: StateChangeRequest,
#     db: Session = Depends(get_db),
#     user=Depends(require_permission(CANDIDATE_UPDATE))  # 👈 THIS LINE
# ):
#     candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
#     if not candidate:
#         raise HTTPException(status_code=404, detail="Candidate not found")

#     try:
#         current_state = CandidateState(candidate.current_state)
#     except ValueError:
#         raise HTTPException(500, "Invalid candidate state in DB")

#     # 1️⃣ Validate state machine
#     try:
#         validate_transition(current_state, data.next_state)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))

#     # 2️⃣ Enforce RBAC
#     if not can_user_transition(user.role, current_state, data.next_state):
#         raise HTTPException(
#             status_code=403,
#             detail="You do not have permission to perform this transition"
#         )

#     # 3️⃣ Write history
#     history = CandidateStateHistory(
#         candidate_id=candidate.id,
#         from_state=current_state.value,
#         to_state=data.next_state.value,
#         reason=data.reason,
#         changed_by=user.id
#     )
#     db.add(history)

#     # 4️⃣ Update state
#     candidate.current_state = data.next_state.value

#     # 5️⃣ Commit
#     db.commit()
#     db.refresh(candidate)

#     return {
#         "candidate_id": candidate.id,
#         "old_state": current_state.value,
#         "new_state": candidate.current_state,
#         "reason": data.reason
#     }

# backend/app/hiring/candidates/routes.py

@router.post("/{candidate_id}/transition")
def change_state(
    candidate_id: UUID,
    data: StateChangeRequest,
    db: Session = Depends(get_db),
    user=Depends(require_permission(CANDIDATE_UPDATE)),
):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    current_state = CandidateState(candidate.current_state)

    # 1️⃣ STATE MACHINE VALIDATION (business rule)
    try:
        validate_transition(current_state, data.next_state)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 2️⃣ RBAC CHECK (security rule)
    if not can_user_transition(user.role, data.next_state):
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to perform this transition"
        )

    # 3️⃣ WRITE AUDIT HISTORY
    history = CandidateStateHistory(
        candidate_id=candidate.id,
        from_state=current_state.value,
        to_state=data.next_state.value,
        reason=data.reason,
        changed_by=user.id,
    )
    db.add(history)

    # 4️⃣ UPDATE CURRENT STATE
    candidate.current_state = data.next_state.value

    # 5️⃣ COMMIT
    db.commit()
    db.refresh(candidate)

    return {
        "candidate_id": candidate.id,
        "old_state": current_state.value,
        "new_state": candidate.current_state,
        "reason": data.reason,
    }



@router.get("/{candidate_id}/timeline")
def get_candidate_timeline(
    candidate_id: UUID,
    db: Session = Depends(get_db),
    user=Depends(require_permission(CANDIDATE_UPDATE))
):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    history = (
        db.query(CandidateStateHistory)
        .filter(CandidateStateHistory.candidate_id == candidate_id)
        .order_by(CandidateStateHistory.changed_at.asc())
        .all()
    )

    return [
        {
            "from_state": h.from_state,
            "to_state": h.to_state,
            "reason": h.reason,
            "changed_by": str(h.changed_by),
            "changed_at": h.changed_at,
        }
        for h in history
    ]

@router.post("/")
def create_candidate(
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    candidate = Candidate(
        name=name,
        email=email,
        current_state=CandidateState.APPLIED.value
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate

