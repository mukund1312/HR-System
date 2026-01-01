from enum import Enum


class RoleEnum(str, Enum):
    MANAGER = "manager"
    INTERVIEWER = "interviewer"
    HR = "hr"
