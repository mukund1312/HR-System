from app.hiring.candidates.states import CandidateState

ALLOWED_TRANSITIONS = {
    CandidateState.APPLIED: {
        CandidateState.L1,
        CandidateState.REJECTED,
    },
    CandidateState.L1: {
        CandidateState.L2,
        CandidateState.REJECTED,
    },
    CandidateState.L2: {
        CandidateState.L3,
        CandidateState.REJECTED,
    },
    CandidateState.L3: {
        CandidateState.HR,
        CandidateState.REJECTED,
    },
    CandidateState.HR: {
        CandidateState.OFFER_SENT,
        CandidateState.REJECTED,
    },
    CandidateState.OFFER_SENT: {
        CandidateState.OFFER_ACCEPTED,
        CandidateState.OFFER_REJECTED,
    },
}

def validate_transition(
    current: CandidateState,
    next_state: CandidateState
):
    allowed = ALLOWED_TRANSITIONS.get(current, set())

    if next_state not in allowed:
        raise ValueError(
            f"Invalid transition from {current} to {next_state}"
        )
