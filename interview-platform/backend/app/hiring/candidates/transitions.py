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
        CandidateState.HR,
        CandidateState.REJECTED,
    },
    CandidateState.HR: {
        CandidateState.OFFER_MADE,
        CandidateState.REJECTED,
    },
    CandidateState.OFFER_MADE: {
        CandidateState.OFFER_ACCEPTED,
        CandidateState.REJECTED,
    },
}
