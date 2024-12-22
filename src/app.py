import gradio as gr
from typing import Dict
import pandas as pd

# from src.application.services import InterviewAnalyzer
# from src.infrastructure.llm import LangchainService
# from src.infrastructure.emotion import DeepFaceService
# from src.infrastructure.speech import GoogleSpeechService


# class GradioInterface:
#     def __init__(self):
#         # Initialize services
#         self.emotion_service = DeepFaceService()
#         self.speech_service = GoogleSpeechService()
#         self.llm_service = LangchainService()
#
#         # Initialize analyzer
#         self.analyzer = InterviewAnalyzer(
#             emotion_service=self.emotion_service,
#             speech_service=self.speech_service,
#             llm_service=self.llm_service,
#         )
#
#     def create_interface(self) -> gr.Interface:
#         def process_submission(
#             video_file: str, resume_file: str, job_requirements: str
#         ) -> Dict:
#             # Implementation for processing submission
#             pass
#
#         # Create Gradio interface
#         interface = gr.Interface(
#             fn=process_submission,
#             inputs=[
#                 gr.Video(label="Interview Recording"),
#                 gr.File(label="Resume"),
#                 gr.Textbox(label="Job Requirements", lines=5),
#             ],
#             outputs=gr.JSON(label="Analysis Results"),
#             title="HR Interview Analysis System",
#             description="Upload interview recording and resume to analyze candidate performance",
#         )
#
#         return interface


# Testing to setup the simple interface
class GradioInterface:
    def __init__(self):
        # DataFrame to List All Users' Feedbacks
        self.candidate_feedback = pd.DataFrame(columns=["Name", "Score", "Feedback"])

    def validate_file_format(self, file_path: str, valid_extensions: list) -> bool:
        return isinstance(file_path, str) and any(
            file_path.endswith(ext) for ext in valid_extensions
        )

    def process_video(self, video_path: str) -> str:
        # Process transcript from the video
        return "### Transcript\nExample of transcript of the interview video."

    def process_resume(self, resume_path: str) -> str:
        # Resume Parsing
        return "### Resume Analysis\n- **Skills**: NLP, Machine Learning, Computer Vision\n- **Experience**: 5 years."

    def analyze_emotions(self, video_path: str) -> str:
        # Emotion Analysis
        return "### Emotion Analysis\n- **Overall Emotion**: Positive\n- **Details**: Candidate displayed confidence and engagement."

    def get_feedback(self, name: str, score: int, feedback: str) -> pd.DataFrame:
        return pd.DataFrame({"Name": [name], "Score": [score], "Feedback": [feedback]})

    def save_report(self):
        # Save report
        report_path = "report_path.docx"
        with open(report_path, "w") as f:
            # Pass fields to include in report here
            f.write("Example report")
        return report_path

    def create_interface(self) -> gr.Blocks:
        def process_submission(
            video_path, resume_path, interview_questions, job_requirements
        ):
            # Validate inputs and formats
            if not video_path:
                return (
                    "Please upload an interview video.",
                    None,
                    None,
                    self.candidate_feedback,
                )
            if not resume_path:
                return (
                    "Please upload a resume (PDF).",
                    None,
                    None,
                    self.candidate_feedback,
                )
            if not interview_questions:
                return (
                    "Please provide interview questions.",
                    None,
                    None,
                    self.candidate_feedback,
                )
            if not job_requirements:
                return (
                    "Please provide job requirements.",
                    None,
                    None,
                    self.candidate_feedback,
                )
            if not self.validate_file_format(video_path, [".mp4", ".avi", ".mkv"]):
                return "Invalid video format.", None, None, self.candidate_feedback
            if not self.validate_file_format(resume_path, [".pdf"]):
                return (
                    "Please submit resume in PDF format.",
                    None,
                    None,
                    self.candidate_feedback,
                )

            # Mock outputs for this submission
            video_transcript = self.process_video(video_path)
            emotion_analysis = self.analyze_emotions(video_path)
            resume_analysis = self.process_resume(resume_path)
            # Example of Feedback
            feedback_list = self.get_feedback(
                name="Johnson",
                score=88,
                feedback="Outstanding technical and soft skills.",
            )
            # Append the new candidate feedback to the DataFrame
            self.candidate_feedback = pd.concat(
                [self.candidate_feedback, feedback_list], ignore_index=True
            )

            # Return both the individual result and the list result
            return (
                video_transcript,
                emotion_analysis,
                resume_analysis,
                self.candidate_feedback,
            )

        # Build the interface using Blocks
        with gr.Blocks() as demo:
            gr.Markdown("## HR Interview Analysis System")

            # Inputs section
            with gr.Row():
                video_input = gr.Video(label="Upload Interview Video")
                resume_input = gr.File(label="Upload Resume (PDF)")
            with gr.Row():
                question_input = gr.Textbox(
                    label="Interview Questions",
                    lines=5,
                    placeholder="Enter the interview question here",
                )
                requirements_input = gr.Textbox(
                    label="Job Requirements",
                    lines=5,
                    placeholder="Enter the job requirements here",
                )

            submit_button = gr.Button("Submit")

            with gr.Tabs():
                with gr.Tab("Result"):
                    transcript_output = gr.Markdown(label="Video Transcript")
                    emotion_output = gr.Markdown(label="Emotion Analysis")
                    resume_output = gr.Markdown(label="Resume Analysis")

                with gr.Tab("List of Candidates"):
                    feedback_output = gr.Dataframe(
                        label="Candidate Feedback Lists", interactive=False
                    )

            save_button = gr.Button("Save Report")
            save_button.click(
                fn=self.save_report,
                inputs=[],
                outputs=gr.File(label="Download Report"),
            )
            # Connect the button to the function
            submit_button.click(
                fn=process_submission,
                inputs=[video_input, resume_input, question_input, requirements_input],
                outputs=[
                    transcript_output,
                    emotion_output,
                    resume_output,
                    feedback_output,
                ],
            )

        return demo


def launch_app():
    print(gr.__version__)
    app = GradioInterface()
    interface = app.create_interface()
    interface.launch()


if __name__ == "__main__":
    launch_app()
