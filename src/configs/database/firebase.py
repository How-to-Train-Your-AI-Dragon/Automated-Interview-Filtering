import firebase_admin
from firebase_admin import credentials, db
import json
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
from uuid_extensions import uuid7
from datetime import datetime

env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

firebase_service_key_str = os.getenv("FIREBASE_API_KEY")

if not firebase_service_key_str:
    raise ValueError("Service account key is not set in the environment variables.")

service_account_key = json.loads(firebase_service_key_str)

service_account_key_path = "/tmp/serviceAccountKey.json"
with open(service_account_key_path, "w") as temp_key_file:
    json.dump(service_account_key, temp_key_file)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key_path

if not firebase_admin._apps:  # Check if already initialized
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": "https://automated-interview-filtering-default-rtdb.asia-southeast1.firebasedatabase.app"
        },
    )

ref = db.reference("interview_results/")
users_ref = ref.child("users")


def write_user_data(
    name, score, interview_question, job_title, job_requirements, feedback
):
    """
    Writes user data to Firebase database with UUID v7.

    Args:
        :param name: Name of the user
        :param score: Interview score
        :param interview_question: Question asked during interview
        :param job_title: Job title
        :param job_requirements: Job requirements
        :param feedback: Feedback for the user

    Returns:
        :return: UUID of the newly created record
    """
    try:
        # Generate UUID v7
        entry_id = str(uuid7())
        timestamp = datetime.now().isoformat()

        if isinstance(score, np.int64):
            score = int(score)
        elif isinstance(score, (float, np.float64)):
            score = int(round(score))

        user_data = {
            "id": entry_id,
            "name": name,
            "score": score,
            "interview_question": interview_question,
            "job_title": job_title,
            "job_requirements": job_requirements,
            "feedback": feedback,
            "created_at": timestamp,
            "updated_at": timestamp,
        }

        # Create a new entry using the UUID as the key
        users_ref.child(entry_id).set(user_data)
        print(f"Data for {name} successfully written to Firebase with ID: {entry_id}")
        return entry_id

    except Exception as e:
        print(f"Error writing data to Firebase: {str(e)}")
        raise


def read_all_users():
    """
    Reads all user data from Firebase database and returns as a pandas DataFrame.

    Returns:
        :return pandas.DataFrame: DataFrame containing all user records with Firebase keys as index
    """
    try:
        users = users_ref.get()
        if not users:
            print("No users found in the database.")
            return pd.DataFrame()

        # Convert Firebase data to DataFrame
        df = pd.DataFrame.from_dict(users, orient="index")

        # Reset index and rename it to 'firebase_key'
        df = df.reset_index().rename(columns={"index": "firebase_key"})

        # Reorder columns to put id and timestamps first
        preferred_order = [
            "firebase_key",
            "id",
            "created_at",
            "updated_at",
            "name",
            "score",
            "interview_question",
            "job_title",
            "job_requirements",
            "feedback",
        ]
        actual_columns = [col for col in preferred_order if col in df.columns]
        remaining_columns = [col for col in df.columns if col not in preferred_order]
        df = df[actual_columns + remaining_columns]

        # Convert timestamps to datetime
        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(df["created_at"])
        if "updated_at" in df.columns:
            df["updated_at"] = pd.to_datetime(df["updated_at"])

        # stream the List[str] feedback to str
        df["feedback"] = df["feedback"].apply(lambda x: " ".join(x))

        df_filtered = df[
            ["name", "job_title", "interview_question", "score", "feedback"]
        ]

        return df_filtered

    except Exception as e:
        print(f"Error reading data from Firebase: {str(e)}")
        raise


def update_user_data(uuid, update_dict):
    """
    Updates existing user data in Firebase database.

    Args:
        :param update_dict: Dictionary containing fields to update
        :param uuid: UUID of the record to update

    Returns:
        :return bool: True if update successful, False otherwise
    """
    try:
        # Get current data
        current_data = users_ref.child(uuid).get()

        if not current_data:
            print(f"No record found with UUID: {uuid}")
            return False

        # Update the timestamp
        update_dict["updated_at"] = datetime.now().isoformat()

        # Update only the specified fields
        users_ref.child(uuid).update(update_dict)
        print(f"Successfully updated record with UUID: {uuid}")
        return True

    except Exception as e:
        print(f"Error updating data in Firebase: {str(e)}")
        raise
