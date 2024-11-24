from enum import Enum, auto


class InterviewStatus(Enum):
    SCHEDULED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    PENDING_REVIEW = auto()
    REVIEWED = auto()
    FAILED = auto()
