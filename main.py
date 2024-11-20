import streamlit as st
from modules.memory import UserMemory
from modules.qa_engine import load_knowledge_base, create_qa_chain
from modules.video_handler import play_video
from modules.quiz_handler import QuizHandler

# Load memory and knowledge base
user_memory = UserMemory()
vector_store = load_knowledge_base("resources/knowledge_base/")
qa_chain = create_qa_chain(vector_store)

# Streamlit UI
st.title("Personalized AI Tutor")

# User authentication
user_id = st.text_input("Enter your username to start:", key="user_id")
if user_id:
    st.write(f"Welcome back, {user_id}!")

    # Retrieve memory
    progress = user_memory.load_memory(user_id)

    # Ask a question
    question = st.text_input("Ask a question:")
    if question:
        answer = qa_chain.run(question)
        st.write(f"Answer: {answer}")

    # Play video tutorial
    video_topic = st.selectbox("Select a topic for a video tutorial:", ["Math", "Science"])
    if st.button("Play Tutorial"):
        play_video(f"resources/videos/{video_topic}.mp4")

    # Take a quiz
    quiz_handler = QuizHandler("resources/quizzes/quiz.json")
    quiz_topic = st.selectbox("Select a topic for a quiz:", ["Math", "Science"])
    if st.button("Take Quiz"):
        quiz = quiz_handler.get_quiz(quiz_topic)
        st.write(f"Quiz: {quiz['question']}")

    # Save progress
    if st.button("Save Progress"):
        user_memory.update_memory(user_id, {"last_topic": quiz_topic})
        st.write("Progress saved!")
