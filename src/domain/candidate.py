from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Candidate:
    id: str
    name: str
    email: str
    resume_data: Dict
    interview_responses: List[str]
    emotional_metrics: Dict
    feedback: Dict
