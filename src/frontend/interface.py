import gradio as gr
from typing import Dict
from src.application.services import InterviewAnalyzer
from src.infrastructure.llm import LangchainService
from src.infrastructure.emotion import DeepFaceService
from src.infrastructure.speech import GoogleSpeechService

class GradioInterface:
    def __init__(self):
        # Initialize services
        self.emotion_service = DeepFaceService()
        self.speech_service = GoogleSpeechService()
        self.llm_service = LangchainService()

        # Initialize analyzer
        self.analyzer = InterviewAnalyzer(
            emotion_service=self.emotion_service,
            speech_service=self.speech_service,
            llm_service=self.llm_service
        )

    def create_interface(self) -> gr.Interface:
        def process_submission(
                video_file: str,
                resume_file: str,
                job_requirements: str
        ) -> Dict:
            # Implementation for processing submission
            pass

        # Create Gradio interface
        interface = gr.Interface(
            fn=process_submission,
            inputs=[
                gr.Video(label="Interview Recording"),
                gr.File(label="Resume"),
                gr.Textbox(label="Job Requirements", lines=5)
            ],
            outputs=gr.JSON(label="Analysis Results"),
            title="HR Interview Analysis System",
            description="Upload interview recording and resume to analyze candidate performance"
        )

        return interface

def launch_app():
    app = GradioInterface()
    interface = app.create_interface()
    interface.launch()

if __name__ == "__main__":
    launch_app()