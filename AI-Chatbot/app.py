import streamlit as st
import random

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []

# Smart Knowledge Base (Keywords)
responses = {
    "ai": "Artificial Intelligence (AI) is the simulation of human intelligence in machines.",
    "machine learning": "Machine Learning is a subset of AI that allows computers to learn from data.",
    "deep learning": "Deep Learning uses neural networks to learn from large amounts of data.",
    "python": "Python is a programming language widely used in AI, data science, and web development.",
    "vertexmind": "VertexMind provides AI internships and learning opportunities.",
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What would you like to know?",
    "who are you": "I am an AI chatbot created using Python and Streamlit.",
    "your name": "I am your AI chatbot assistant.",
    "what can you do": "I can answer basic AI and programming related questions."
}

default_responses = [
    "That's interesting! Tell me more.",
    "I'm still learning. Can you ask something else?",
    "I'm not sure, but I'm learning every day.",
    "Can you rephrase your question?"
]

# User input
user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append(("You", user_input))

    user_input_lower = user_input.lower()
    found = False

    for keyword in responses:
        if keyword in user_input_lower:
            answer = responses[keyword]
            found = True
            break

    if not found:
        answer = random.choice(default_responses)

    st.session_state.messages.append(("AI", answer))

# Display chat
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")