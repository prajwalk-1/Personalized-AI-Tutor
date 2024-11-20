# Personalized AI Tutor

## Objective
The **Personalized AI Tutor** is an AI-powered educational assistant that adapts to a user's learning style and helps improve the learning experience. By utilizing LangChain, this system retrieves context-specific information from various educational resources such as textbooks, PDFs, online courses, and more. It aims to provide an interactive, adaptive, and efficient learning experience across various subjects.

This project combines multiple AI technologies like natural language processing (NLP), embeddings, and retrieval-augmented generation (RAG) for personalized tutoring. It supports interactive Q&A, quiz management, video tutorials, and memory tracking of the user’s progress.

## Key Features
- **Interactive Q&A**: Get answers to questions in various subjects based on the curated knowledge base (textbooks, PDFs, online courses).
- **Memory System**: Tracks and stores user progress, improving interaction by remembering past topics and performance.
- **Video Tutorials**: Integrates educational video tutorials for better understanding of complex concepts.
- **Quizzes**: Provides quizzes to test and reinforce knowledge on various topics.

## Applications
- **Online Learning Platforms**: The AI tutor can be integrated into e-learning platforms, providing personalized assistance to students in real-time.
- **Personal Study Assistant**: Ideal for self-learners who need interactive support while studying.
- **Corporate Training**: Useful for companies offering continuous learning programs to their employees.
- **Subject-Specific Tutoring**: Can be customized for various subjects like mathematics, science, history, and more.

## Technologies Used
- **LangChain**: For efficient language model interaction and retrieval-augmented generation (RAG).
- **OpenAI API**: For accessing language models to answer questions and generate content.
- **Streamlit**: For building an interactive web interface.
- **Python**: Core language for implementing the backend logic.
- **Flask (optional)**: For serving the application as a web app if needed.
- **python-dotenv**: To securely handle API keys and configuration.

## Folder Structure
```
ai_tutor/
│
├── main.py                # Entry point of the application
├── requirements.txt       # Dependencies
├── config.py              # Configuration and settings
├── resources/
│   ├── knowledge_base/    # Educational resources (PDFs, text files, etc.)
│   ├── quizzes/           # Quiz files
│   └── videos/            # Video tutorials
├── modules/
│   ├── memory.py          # User progress tracking
│   ├── qa_engine.py       # Question-Answering Engine
│   ├── video_handler.py   # Video tutorial integration
│   ├── quiz_handler.py    # Quiz management
└── README.md              # Project documentation
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prajwalk-1/Personalized-AI-Tutor.git
   cd Personalized-AI-Tutor
   

2. **Install dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**:
   ```bash
   streamlit run main.py
   ```

   If using Flask instead of Streamlit, you can run the app as follows:
   ```bash
   python main.py
   ```

## Configuration
### `config.py`
- This file contains configuration settings, including the path to educational resources and API keys. The API key for OpenAI is loaded from the `.env` file.

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## Features and Explanation

### 1. **Interactive Q&A System**
   - The core of the AI Tutor is its ability to answer questions from the user.
   - **LangChain** is used for interacting with the OpenAI API and querying relevant information from the knowledge base (textbooks, PDFs, etc.).
   - The system can fetch, process, and present data to the user based on the context of their query.

### 2. **Memory System**
   - The **Memory module** tracks user progress. It stores previously asked questions and responses to provide personalized tutoring.
   - This feature helps the system to adapt to the user's learning pace and topics of interest.

### 3. **Video Tutorials Integration**
   - Video tutorials are integrated within the system to provide visual explanations for complex topics.
   - Users can watch relevant video tutorials as part of their learning path.

### 4. **Quizzes**
   - The system can serve quizzes on various subjects from the `resources/quizzes/` folder.
   - After completing quizzes, the tutor can provide immediate feedback to help reinforce the material learned.

## Advantages
- **Personalized Learning**: Adapts to the user's pace, interests, and learning style.
- **Comprehensive**: Combines multiple forms of learning including Q&A, video tutorials, and quizzes.
- **Interactive and Engaging**: Makes learning more engaging with interactive sessions and real-time feedback.
- **Scalable**: The system can scale to include new topics, quizzes, videos, and more educational resources.
- **Real-Time Updates**: Integrates knowledge dynamically, so the tutor always stays updated with the latest educational material.

## Example Use Case
- A student studying biology can ask questions about cell structure or genetics. The AI tutor retrieves answers from textbooks and online educational resources, presents the information in an easy-to-understand manner, and can suggest relevant video tutorials and quizzes to help the student test their understanding.

## Future Enhancements
- **Adaptive Learning Paths**: Implement machine learning algorithms to create adaptive learning paths based on the user’s progress.
- **Speech Integration**: Add voice recognition for interactive, hands-free sessions.
- **Performance Analytics**: Visualize user progress through charts and graphs to help students track their learning journey.

## Requirements

### Python Libraries:
- `streamlit` for web app
- `openai` for interacting with OpenAI's API
- `langchain` for managing document retrieval and processing
- `python-dotenv` for environment variable management
- `pandas` for data manipulation (if required)
- `numpy` and `scikit-learn` for any ML-related enhancements

### Hardware:
- A machine with an internet connection to access OpenAI's API.
- GPU (optional, for faster model inference).
