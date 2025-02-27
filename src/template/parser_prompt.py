from llama_index.core.prompts import PromptTemplate

PARSE_RESUME_PROMPT = """
You are tasked with parsing a resume.

**Your Focus**: 
 - Reproduce only the main body text, including section headers and bullet points, exactly as received.
 - Do not skip section numbers in the format DIGIT.DIGIT (e.g., 10.1, 3.1), you must apply a markdown header level based on the depth (e.g., # for main sections, ## for subsections) to reflect the appropriate hierarchy, and output them.
 - Do make sure that section numbers are always followed by the corresponding section title without a '\n' character in between or separating them into different headers. Valid examples are as below:
     - '# 14 Experience'
     - '# 2 Education'
   Invalid examples are as below:
     - '# 14\n # Experience'
     - '# 2\n # Education'
 - You may only add markdown header symbols (#, ##, ###, etc.) to denote the hierarchical levels of section headers.
 - Do not make up any text and headers that are not present in the original text.

**Expected Output**:
 - Text, section headers, and bullet points must be reproduced without any text edits, additions, or deletions, other than adding markdown header symbols (#, ##, ###, etc.).
 - Use markdown headers to denote additional hierarchy (e.g., # for main sections, ## for subsections) based on the best interpretation of the document’s structure.
"""
