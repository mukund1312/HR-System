# from app.auth.roles import RoleEnum
# from app.hiring.candidates.states import CandidateState
# from app.hiring.candidates.state_machine import validate_transition

# # STATE_ROLE_MAP = {
# #     CandidateState.APPLIED: {RoleEnum.HR},

# #     CandidateState.L1: {RoleEnum.INTERVIEWER},
# #     CandidateState.L2: {RoleEnum.INTERVIEWER},
# #     CandidateState.L3: {RoleEnum.INTERVIEWER},

# #     CandidateState.HR: {RoleEnum.HR},

# #     CandidateState.OFFER_SENT: {RoleEnum.HR},
# #     CandidateState.OFFER_ACCEPTED: {RoleEnum.HR},
# #     CandidateState.OFFER_REJECTED: {RoleEnum.HR},

# #     CandidateState.REJECTED: {RoleEnum.HR},
# # }



# # # def can_user_transition(user_role: RoleEnum, next_state: CandidateState) -> bool:
# # #     allowed_roles = STATE_ROLE_MAP.get(next_state, set())
# # #     return user_role in allowed_roles
# # def can_user_transition(user_role, current_state, next_state):
# #     if user_role not in STATE_ROLE_MAP.get(next_state, set()):
# #         return False

# #     # Optional: enforce valid state sequence
# #     try:
# #         validate_transition(current_state, next_state)
# #     except ValueError:
# #         return False

# #     return True
# from fastapi import HTTPException

# from app.auth.roles import RoleEnum
# from app.hiring.candidates.states import CandidateState
# from app.hiring.candidates.state_machine import validate_transition

# STATE_ROLE_MAP = {
#     CandidateState.APPLIED: {RoleEnum.HR,RoleEnum.INTERVIEWER},

#     CandidateState.L1: {RoleEnum.INTERVIEWER},
#     CandidateState.L2: {RoleEnum.INTERVIEWER},
#     CandidateState.L3: {RoleEnum.INTERVIEWER},

#     CandidateState.HR: {RoleEnum.HR},

#     CandidateState.OFFER_SENT: {RoleEnum.HR},
#     CandidateState.OFFER_ACCEPTED: {RoleEnum.HR},
#     CandidateState.OFFER_REJECTED: {RoleEnum.HR},

#     CandidateState.REJECTED: {RoleEnum.HR},
# }

# def can_user_transition(user_role: RoleEnum,# current_state: CandidateState,
#     next_state: CandidateState
# ) :
#     # 1️⃣ Validate state machine rule
# # state machine check
#     validate_transition(current_state, data.next_state)

# # RBAC check
#     if not can_user_transition(user.role, data.next_state):
#         raise HTTPException(
#         status_code=403,
#         detail="You do not have permission to perform this transition"
#     )


# backend/app/hiring/candidates/permissions.py

from app.auth.roles import RoleEnum
from app.hiring.candidates.states import CandidateState

STATE_ROLE_MAP = {
    CandidateState.APPLIED: {RoleEnum.HR, RoleEnum.MANAGER},

    CandidateState.L1: {RoleEnum.INTERVIEWER},
    CandidateState.L2: {RoleEnum.INTERVIEWER},
    CandidateState.L3: {RoleEnum.INTERVIEWER},

    CandidateState.HR: {RoleEnum.HR},

    CandidateState.OFFER_SENT: {RoleEnum.HR},
    CandidateState.OFFER_ACCEPTED: {RoleEnum.HR},
    CandidateState.OFFER_REJECTED: {RoleEnum.HR},

    CandidateState.REJECTED: {RoleEnum.HR},
}

def can_user_transition(user_role: RoleEnum, next_state: CandidateState) -> bool:
    """
    RBAC ONLY.
    Answers: Is this role allowed to move candidate INTO next_state?
    """
    allowed_roles = STATE_ROLE_MAP.get(next_state, set())
    return user_role in allowed_roles
