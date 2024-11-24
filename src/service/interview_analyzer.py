from src.domain.enums.file_types import VideoFileType
from src.domain.enums.emotion_types import EmotionType
from src.domain.entities.interview import Interview
from typing import Dict, List


class InterviewAnalyzer:
    def validate_video(self, video_path: str) -> bool:
        file_extension = video_path[video_path.rfind(".") :]
        return VideoFileType.validate_format(file_extension)

    def analyze_emotions(
        self, emotion_data: Dict[str, float]
    ) -> Dict[EmotionType, float]:
        analyzed_emotions = {}
        for emotion_name, score in emotion_data.items():
            try:
                emotion_type = EmotionType(emotion_name.lower())
                analyzed_emotions[emotion_type] = score
            except ValueError:
                continue
        return analyzed_emotions

    def get_dominant_emotion(
        self, emotion_scores: Dict[EmotionType, float]
    ) -> EmotionType:
        return max(emotion_scores.items(), key=lambda x: x[1])[0]

    def is_positive_response(self, emotion_scores: Dict[EmotionType, float]) -> bool:
        positive_emotions = EmotionType.get_positive_emotions()
        dominant_emotion = self.get_dominant_emotion(emotion_scores)
        return dominant_emotion in positive_emotions
