from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
from src.domain.enums.interview_status import InterviewStatus
from src.domain.enums.emotion_types import EmotionType

@dataclass
class Interview:
    id: str
    candidate_id: str
    job_id: str
    video_path: str
    status: InterviewStatus
    questions: List[str]
    responses_transcription: List[str]
    timestamp: datetime
    duration: int
    emotional_analysis: Dict[EmotionType, float]

    def is_completed(self) -> bool:
        return self.status == InterviewStatus.COMPLETED

    def is_reviewable(self) -> bool:
        return self.status in [InterviewStatus.COMPLETED, InterviewStatus.PENDING_REVIEW]