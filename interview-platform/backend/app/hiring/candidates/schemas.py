from datetime import datetime
from typing import Optional
from pydantic import BaseModel
# from pydantic import BaseModel
# from typing import Optional
from app.hiring.candidates.states import CandidateState


class StateChangeRequest(BaseModel):
    next_state: CandidateState
    reason: Optional[str] = None


class CandidateTimelineEvent(BaseModel):
    from_state: str
    to_state: str
    reason: Optional[str]
    changed_by: str
    changed_at: datetime

    class Config:
        from_attributes = True

