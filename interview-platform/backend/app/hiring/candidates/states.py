from enum import Enum

class CandidateState(str, Enum):
    APPLIED = "applied"
    L1 = "l1_interview"
    L2 = "l2_interview"
    L3 = "l3_interview"
    HR = "hr_round"
    OFFER_SENT = "offer_sent"
    OFFER_ACCEPTED = "offer_accepted"
    OFFER_REJECTED = "offer_rejected"
    REJECTED = "rejected"
