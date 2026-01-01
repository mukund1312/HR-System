from app.core.permissions import *

ROLE_PERMISSIONS = {
    "manager": {
        CANDIDATE_READ,
        CANDIDATE_UPDATE,
        CANDIDATE_DELETE,
        INTERVIEW_SCHEDULE,
        INTERVIEW_FEEDBACK,
    },
    "hr": {
        CANDIDATE_READ,
        INTERVIEW_SCHEDULE,
        RESUME_GENERATE,
        RESUME_EXPORT,
    },
    "interviewer": {
        CANDIDATE_READ,
        CANDIDATE_UPDATE,
        INTERVIEW_FEEDBACK
        
    },
}
