import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import Base


class CandidateStateHistory(Base):
    __tablename__ = "candidate_state_history"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    candidate_id = Column(
        UUID(as_uuid=True),
        ForeignKey("candidates.id"),
        nullable=False
    )

    from_state = Column(String, nullable=False)

    to_state = Column(String, nullable=False)

    reason = Column(String, nullable=True)

    # changed_by = Column(
    #     UUID(as_uuid=True),
    #     ForeignKey("users.id"),
    #     nullable=False
    # )
    # candidate_state_history.py
    changed_by = Column(String, nullable=False)


    changed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
