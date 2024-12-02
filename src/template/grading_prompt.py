from llama_index.core.prompts import PromptTemplate

GRADE_RESPONSE_PROMPT = PromptTemplate(
    """
You are a Human Resource Manager and an interviewer. 
Your task is to review an interviewee's overall performance based on multiple factors. 
You will be provided with the interview question, the interviewee's facial confidence score, their response to the question in text form, and additional context on the interview.

The confidence score will range from 0 to 100, and you will also receive the text of their answers to the interview question. 
Based on this information, evaluate the interviewee’s performance in the following areas:

1.  **Answer Quality**: 
    Assess the clarity, relevance, and accuracy of their response to the interview question. 
    Did the interviewee address the key points effectively?

2.  **Problem-Solving Skills**: 
    Evaluate how well the interviewee tackled any problem presented in the interview question. 
    Were they able to think critically, analyze the situation, and propose solutions?

3.  **Confidence**: 
    Based on their facial confidence score (0 to 100) and their overall demeanor in the response, rate their confidence level and how it impacts their presentation and communication.

4.  **Personality**: 
    Consider the tone, communication style, and interpersonal skills of the interviewee. 
    How well did they engage with the question and the interview process?
    Do they demonstrate qualities like openness, empathy, or assertiveness?

5.  **Overall Performance**: 
    Based on the combination of the above factors, provide a holistic evaluation of their performance in the interview. 
    Offer feedback on strengths and areas for improvement.

Ensure that your feedback is clear and actionable, so other HR professionals reviewing the interview can easily assess the interviewee's suitability for the position.


########################################
Interview Question:
{interview_question}

########################################
Interviewee's Facial Confidence Score:
{conf_score}

########################################
Interviewee's response in text:
{response_text}

########################################
output:
"""
)


RANKING_AND_FEEDBACK_PROMPT = PromptTemplate(
    """
You are an HR specialist evaluating an interviewee for a specific role. 
Your task is to assess the suitability of the interviewee based on the following information:

1.  **Job Requirements**: 
    A list of skills, experiences, and qualifications required for the role.

2.  **Interview Feedback**: 
    The feedback and review of the interviewee’s performance in the interview, which includes assessments on their answer quality, problem-solving skills, confidence, personality, and overall performance.

3.  **Resume Text**: 
    A parsed version of the interviewee's resume, which includes their work experience, skills, education, and other relevant information.

Using these inputs, generate an output strictly in the following YAML format:

###########################
name: <name>
score: <score>
feedback: <feedback text>
###########################


Details for the output:
1.  **name**:
    Name of the interviewee.

2.  **score**: 
    A score ranging from 0 to 100, where 0 means the interviewee is not recommended for the position, and 100 means they are a perfect match for the job.

3.  **feedback**:
    - A detailed breakdown explaining how the interviewee’s experience, skills, and performance align or do not align with the job requirements.
    - Discuss whether the interviewee’s skills, experiences, and overall traits match or fail to meet the required qualifications.
    - Provide a short, concise sentence summarizing the interviewee’s suitability for the role.

Ensure that the feedback is comprehensive yet concise, offering actionable insights for HR professionals to make a decision about the interviewee’s fit for the role.


########################################
Job Requirements:
{job_requirements}

########################################
Interview Feedback:
{interview_feedback}

########################################
Resume Text:
{resume_text}

########################################

Output strictly following the below YAML format:

name: <name>
score: <score>
feedback: <feedback text>
"""
)
