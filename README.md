---
title: Automated Interview Filtering
emoji: 🐉
colorFrom: red
colorTo: purple
sdk: gradio
sdk_version: "5.6.0"
app_file: src/app.py
pinned: true
---

[![Sync to Hugging Face hub](https://github.com/How-to-Train-Your-AI-Dragon/Automated-Interview-Filtering/actions/workflows/main.yml/badge.svg)](https://github.com/How-to-Train-Your-AI-Dragon/Automated-Interview-Filtering/actions/workflows/main.yml)

# Automated Interview Filtering

## Overview
The Automated Interview Filtering System is an AI-powered tool that helps HR professionals streamline their interview process through automated analysis of video interviews, resumes, and candidate responses. The system leverages multiple AI technologies including emotion detection, speech-to-text conversion, and natural language processing to provide comprehensive candidate assessments.

## Architecture
The project follows a clean, **layered monolith architecture**:

```
src/
├── domain/      # Core business logic and entities
├── service/     # Use cases and business rules
├── utils/       # Helper functions and utilities
└── app.py       # Frontend interface
tests/
└── integration/ # Integration tests
```

### Key Components
- **Domain Layer**: Contains business entities, value objects, and enums
- **Service Layer**: Core business logic and use cases
    - LangChain for LLM integration
    - DeepFace for emotion analysis
    - Google Speech-to-Text for audio transcription
    - LlamaParse for resume parsing
- **Frontend Interface**: Gradio-based user interface
- **Utils**: Helper functions and utilities

## Technologies Used
- **Frontend**: Gradio
- **AI/ML**:
    - LangChain for LLM operations
    - DeepFace for facial emotion analysis
    - Google Speech-to-Text API
    - LlamaParse for resume parsing
- **Development Tools**:
    - Python 3.9+
    - Black for code formatting
    - pytest for testing
    - pre-commit hooks

## Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/How-to-Train-Your-AI-Dragon/Automated-Interview-Filtering.git
cd automated-interview-filtering
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configurations
```

## Development Setup

### Code Formatting
We use Black for code formatting. To set up:

1. Install black and pre-commit:
```bash
pip install black pre-commit
```

2. Run pre-commit hooks:
```bash
pre-commit install
```

3. Run Black manually:
```bash
black .
```

4. Configure VS Code (optional):
```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

Refer to the [Black documentation](https://black.readthedocs.io/en/stable/) for more information. Reference from the article [here](https://dev.to/emmo00/how-to-setup-black-and-pre-commit-in-python-for-auto-text-formatting-on-commit-4kka)

### Git Workflow

#### Creating a New Branch
```bash
# Update main branch
git checkout main
git pull origin main

# Create new feature branch
git checkout -b feature/your-feature-name
```

#### Making Changes
```bash
# Stage changes
git add .

# Commit changes
git commit -m "feat: your descriptive commit message"

# Push to remote
git push origin feature/your-feature-name
```

### Running the Application

#### Starting Gradio Interface
```bash
python -m src.presentation.gradio.interface
```
The interface will be available at `http://localhost:7860`

#### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_interview_analyzer.py

# Run with coverage
pytest --cov=src tests/
```

## Configuration

### Environment Variables
```env
OPENAI_API_KEY=your_key_here
GOOGLE_SPEECH_KEY=your_key_here
LLAMAPARSE_API_KEY=your_key_here
```

### Supported File Formats
- Video: MP4, AVI, MOV, WMV
- Resume: PDF, DOCX, DOC, TXT

## Error Handling
The system implements comprehensive error handling for:
- Invalid file formats
- API failures
- Resource limitations
- Processing errors

## Contributing
1. Clone the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Commit Message Format
```
[<type>]: <subject>

[<body>]

[<footer>]
```
Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring

## License
This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more information.
