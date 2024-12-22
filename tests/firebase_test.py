import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.configs.database.firebase import (
    read_all_users,
    write_user_data,
    update_user_data,
)


# Mock data for tests
MOCK_USER_DATA = {
    "uuid7-1": {
        "id": "uuid7-1",
        "name": "Alice",
        "score": 90,
        "job_title": "Software Engineer",
        "interview_question": "What are your strengths?",
        "job_requirements": "Team player",
        "feedback": "Excellent response.",
        "created_at": "2024-01-01T10:00:00",
        "updated_at": "2024-01-01T10:00:00",
    },
    "uuid7-2": {
        "id": "uuid7-2",
        "name": "Bob",
        "score": 85,
        "job_title": "Software Engineer",
        "interview_question": "Describe your work ethic.",
        "job_requirements": "Self-starter",
        "feedback": "Good examples provided.",
        "created_at": "2024-01-02T10:00:00",
        "updated_at": "2024-01-02T10:00:00",
    },
}


@patch("src.configs.database.firebase.users_ref")  # Mock Firebase reference
def test_write_user_data(mock_users_ref):
    mock_users_ref.child.return_value.set = MagicMock()

    name = "Charlie"
    score = 88
    job_title = "Software Engineer"
    interview_question = "How do you handle challenges?"
    job_requirements = "Problem solver"
    feedback = "Well-articulated response."

    entry_id = write_user_data(
        name, score, interview_question, job_title, job_requirements, feedback
    )

    # Check that Firebase `set` was called with correct data
    mock_users_ref.child.assert_called_with(entry_id)
    mock_users_ref.child(entry_id).set.assert_called_once()


@patch("src.configs.database.firebase.users_ref")
def test_read_all_users(mock_users_ref):
    # Mock the Firebase `get` method
    mock_users_ref.get.return_value = MOCK_USER_DATA

    df = read_all_users()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "name" in df.columns


@patch("src.configs.database.firebase.users_ref")
def test_update_user_data(mock_users_ref):
    mock_users_ref.child.return_value.get.return_value = MOCK_USER_DATA["uuid7-1"]
    mock_users_ref.child.return_value.update = MagicMock()

    uuid = "uuid7-1"
    update_dict = {"score": 95, "feedback": "Updated feedback."}

    result = update_user_data(uuid, update_dict)

    assert result is True
    mock_users_ref.child.assert_called_with(uuid)
    mock_users_ref.child(uuid).update.assert_called_once_with(update_dict)


@patch("src.configs.database.firebase.users_ref")
def test_update_user_data_no_record(mock_users_ref):
    mock_users_ref.child.return_value.get.return_value = None

    uuid = "non-existent-uuid"
    update_dict = {"score": 95, "feedback": "Updated feedback."}

    result = update_user_data(uuid, update_dict)

    assert result is False
    mock_users_ref.child.assert_called_with(uuid)
