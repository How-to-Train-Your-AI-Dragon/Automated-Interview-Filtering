from enum import Enum


class EmotionType(Enum):

    SAD = "sad"
    FEAR = "fear"
    ANGRY = "angry"
    DISGUST = "disgust"

    HAPPY = "happy"
    NEUTRAL = "neutral"
    SURPRISE = "surprise"

    @classmethod
    def get_positive_emotions(cls):
        return [cls.HAPPY, cls.NEUTRAL, cls.SURPRISE]

    @classmethod
    def get_negative_emotions(cls):
        return [cls.SAD, cls.FEAR, cls.ANGRY, cls.DISGUST]
