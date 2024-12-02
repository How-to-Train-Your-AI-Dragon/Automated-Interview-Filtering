import cv2
import yaml
import numpy as np
from pathlib import Path
import speech_recognition as sr
from moviepy import VideoFileClip


def extract_audio(
    input_video_file: str = "",
    output_audio_file: str = "",
) -> str:
    """
    Extracts audio from input video file, and save it to the respective path.
    Returns the path to the saved audio file if extraction is successful.
    Supported input video file formats are:
     - .mp4
     - .mov

    Supported output audio file formats are:
     - .wav
    """
    try:
        input_video_file = str(Path(input_video_file))
        output_audio_file = str(Path(output_audio_file))

        # Load the video file
        video = VideoFileClip(input_video_file)

        # Extract audio and write to output file
        video.audio.write_audiofile(output_audio_file)

        print(f"[extract_audio()] : Audio extracted and saved to {output_audio_file}")

        return output_audio_file
    except Exception as e:
        print(e)
        return None


def audio2text(audio_file: str = "") -> str:
    """
    Converts audio to text using Google's text-to-audio engine (Local),
    and returns the text.
    """
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    return text


def sample_frames(input_video_file: str = "", sample_rate: int = 2) -> list[np.ndarray]:
    """
    Samples one frame every 'sample_rate' frames from the video file and returns
    them in the form of a list of Numpy ndarray objects.
    """
    cap = cv2.VideoCapture(input_video_file)
    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % sample_rate == 0:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        count += 1
    cap.release()

    return frames


def parse_yaml_string(
    yaml_string: str = "", expected_keys: list[str] = None, cleanup: bool = True
) -> dict:
    """
    Parses a YAML string into a Python dictionary based on a list of
    expected keys.
    """

    # removes ```YAML ``` heading and footers if present
    if cleanup:
        yaml_string = yaml_string.replace("YAML", "")
        yaml_string = yaml_string.replace("yaml", "")
        yaml_string = yaml_string.replace("`", "")

    try:
        parsed_data = yaml.safe_load(yaml_string)

        # Handle missing keys with error handling
        result = {}
        for key in expected_keys:
            if key in parsed_data:
                result[key] = parsed_data[key]
            else:
                print(f"[parse_yaml_string()] : Missing key {key}")

        return result

    except KeyError as e:
        print(e)
        return None
