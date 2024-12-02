import numpy as np
from deepface import DeepFace

from src.domain.enums.emotion_types import EmotionType


class EmotionRecognition:
    def __init__(self):
        pass

    @classmethod
    def detect_face_emotions(cls, frames: list[np.ndarray] = None) -> list:
        """
        Performs facial emotion detection using the DeepFace model
        """
        emotions = []
        for frame in frames:
            frame_result = DeepFace.analyze(
                frame, actions=["emotion"], enforce_detection=False
            )
            emotions.append(frame_result)

        return emotions

    @classmethod
    def process_emotions(cls, emotions: list) -> dict:
        """
        Processes the emotions by calculating the overall confidence score using a
        custom weighted emotion balancing algorithm.

        Returns:
        - weighted normalized score
        - signed, weighted normalized score
        - confidence score
        """

        count = 0
        emots = {
            str(EmotionType.SAD.value): 0,
            str(EmotionType.FEAR.value): 0,
            str(EmotionType.ANGRY.value): 0,
            str(EmotionType.DISGUST.value): 0,
            str(EmotionType.HAPPY.value): 0,
            str(EmotionType.NEUTRAL.value): 0,
            str(EmotionType.SURPRISE.value): 0,
        }

        for frame_result in emotions:
            if len(frame_result) > 0:
                emot = frame_result[0]["emotion"]
                emots[str(EmotionType.SAD.value)] = (
                    emots.get(str(EmotionType.SAD.value), 0)
                    + emot[str(EmotionType.SAD.value)]
                )
                emots[str(EmotionType.FEAR.value)] = (
                    emots.get(str(EmotionType.FEAR.value), 0)
                    + emot[str(EmotionType.FEAR.value)]
                )
                emots[str(EmotionType.ANGRY.value)] = (
                    emots.get(str(EmotionType.ANGRY.value), 0)
                    + emot[str(EmotionType.ANGRY.value)]
                )
                emots[str(EmotionType.DISGUST.value)] = (
                    emots.get(str(EmotionType.DISGUST.value), 0)
                    + emot[str(EmotionType.DISGUST.value)]
                )
                emots[str(EmotionType.HAPPY.value)] = (
                    emots.get(str(EmotionType.HAPPY.value), 0)
                    + emot[str(EmotionType.HAPPY.value)]
                )
                emots[str(EmotionType.NEUTRAL.value)] = (
                    emots.get(str(EmotionType.NEUTRAL.value), 0)
                    + emot[str(EmotionType.NEUTRAL.value)]
                )
                emots[str(EmotionType.SURPRISE.value)] = (
                    emots.get(str(EmotionType.SURPRISE.value), 0)
                    + emot[str(EmotionType.SURPRISE.value)]
                )
                count += 1

        # prevent zero division
        if count == 0:
            count = 1

        for i in list(emots.keys()):
            emots[i] /= count * 100

        # refactor according to custom weightage
        sad_score = emots[str(EmotionType.SAD.value)] * 1.3
        fear_score = emots[str(EmotionType.FEAR.value)] * 1.3
        angry_score = emots[str(EmotionType.ANGRY.value)] * 1.3
        disgust_score = emots[str(EmotionType.DISGUST.value)] * 10
        happy_score = emots[str(EmotionType.HAPPY.value)] * 1.7
        neutral_score = emots[str(EmotionType.NEUTRAL.value)] / 1.2
        surprise_score = emots[str(EmotionType.SURPRISE.value)] * 1.4

        score_list = [
            sad_score,
            angry_score,
            surprise_score,
            fear_score,
            happy_score,
            disgust_score,
            neutral_score,
        ]
        min_value = min(score_list)
        max_value = max(score_list)
        normalized_scores = [
            (score - min_value) / (max_value - min_value) for score in score_list
        ]
        mean = np.mean(normalized_scores)

        result_scores = [
            (-sad_score),
            (-angry_score),
            surprise_score,
            (-fear_score),
            happy_score,
            (-disgust_score),
            neutral_score,
        ]
        min_value = min(result_scores)
        max_value = max(result_scores)
        normalized_result_scores = [
            (score - min_value) / (max_value - min_value) for score in result_scores
        ]
        result = np.mean(normalized_result_scores)

        difference = abs((mean - result) / mean) * 100

        # keep values in range of [0, 100]
        if difference > 50:
            difference = 50

        if mean > result:
            conf = 50 - difference
        else:
            conf = 50 + difference

        return {"mean": mean, "result": result, "conf": conf}
