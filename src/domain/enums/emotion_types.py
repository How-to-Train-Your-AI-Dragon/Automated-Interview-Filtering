from enum import Enum

class EmotionType(Enum):
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    NEUTRAL = "neutral"
    SURPRISED = "surprised"
    FEARFUL = "fearful"
    DISGUSTED = "disgusted"

    @classmethod
    def get_positive_emotions(cls):
        return [cls.HAPPY, cls.NEUTRAL]

    @classmethod
    def get_negative_emotions(cls):
        return [cls.SAD, cls.ANGRY, cls.FEARFUL, cls.DISGUSTED]