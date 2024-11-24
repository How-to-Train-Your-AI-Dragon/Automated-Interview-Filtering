from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Resume:
    id: str
    candidate_id: str
    file_path: str
    parsed_content: Dict
    skills: List[str]
    experience: List[Dict]
    education: List[Dict]
