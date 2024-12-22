import pytest
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.service.emotion_recognition import EmotionRecognition


# Mock EmotionType enum for testing
class MockEmotionType:
    SAD = "SAD"
    FEAR = "FEAR"
    ANGRY = "ANGRY"
    DISGUST = "DISGUST"
    HAPPY = "HAPPY"
    NEUTRAL = "NEUTRAL"
    SURPRISE = "SURPRISE"


EmotionType = MockEmotionType


@pytest.fixture
def mock_frames():
    # Create mock frames as numpy arrays
    return [
        np.random.rand(224, 224, 3),
        np.random.rand(224, 224, 3),
    ]


@pytest.fixture
def mock_emotions():
    # Create mock DeepFace results
    return [
        {
            "emotion": {
                "SAD": 10,
                "FEAR": 5,
                "ANGRY": 15,
                "DISGUST": 2,
                "HAPPY": 50,
                "NEUTRAL": 10,
                "SURPRISE": 8,
            }
        },
        {
            "emotion": {
                "SAD": 20,
                "FEAR": 10,
                "ANGRY": 10,
                "DISGUST": 5,
                "HAPPY": 40,
                "NEUTRAL": 15,
                "SURPRISE": 5,
            }
        },
    ]


def test_normalize_scores():
    scores = [10, 20, 30, 40]
    normalized_scores = EmotionRecognition._EmotionRecognition__normalize_scores(scores)

    assert len(normalized_scores) == len(scores)
    assert min(normalized_scores) == 0
    assert max(normalized_scores) == 1
