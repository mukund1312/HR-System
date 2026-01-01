from app.hiring.candidates.states import CandidateState
from app.hiring.candidates.transitions import ALLOWED_TRANSITIONS


def validate_transition(current: CandidateState, next_state: CandidateState):
    if current == next_state:
        raise ValueError("Candidate is already in this state")

    allowed = ALLOWED_TRANSITIONS.get(current, set())

    if next_state not in allowed:
        raise ValueError(
            f"Invalid transition from {current.value} to {next_state.value}"
        )

