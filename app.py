import streamlit as st
import requests
import time

# Initialize session state variables for storing chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to send user message to the Rasa server and get a response
def get_bot_response(user_input):
    try:
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        headers = {"Content-Type": "application/json"}
        data = {"sender": "user", "message": user_input}

        response = requests.post(rasa_url, json=data, headers=headers)
        if response.status_code == 200:
            bot_responses = response.json()
            if bot_responses:
                # Concatenate all bot responses
                bot_reply = "<br>".join([resp.get("text", "") for resp in bot_responses])
                return bot_reply if bot_reply else "No response"
            else:
                return "No response from the bot."
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# UI
st.set_page_config(page_title="Learning Chatbot", page_icon="🤖", layout="wide")
st.title("🌟 Ask the Learning Bot 🌟")

# Sidebar
# Sidebar with unique and engaging text
st.sidebar.title("🎓 Your Personalized Learning Companion")
st.sidebar.write("""
    🌟 Looking for learning resources?
    📚 Get book recommendations!
    🤖 Ask the bot for insightful explanations!
    💡 Enhance your knowledge in various fields.
    🎯 Let me guide you in your learning journey!
""")

# Input field for user message
user_input = st.text_input("Type your message here 👇", placeholder="e.g., Tell me more about Python", key="user_input")


# Send button to submit the user input
if st.button("Send", key="send_message"):
    if user_input.strip():
        with st.spinner('Thinking...'):
            # Get bot response
            bot_response = get_bot_response(user_input)
            
            # Append user input and bot response to chat history
            st.session_state.chat_history.append(f'<p class="user-message">You:</p> {user_input}')
            st.session_state.chat_history.append(f'<p class="bot-message">Bot:</p> {bot_response}')
            
    else:
        st.warning("Please enter a message.")



# UI


# Set a custom background
st.markdown("""
    <style>
        .css-1d391kg {background-color: #F3F7FA; padding: 20px;}
        .css-1b6t4n4 {color: #004d8c; font-size: 28px;}
        .chatbox {background-color: grey; border-radius: 8px; padding: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); height: 400px; overflow-y: auto;}
        .user-message, .bot-message {
            color: #3366cc; 
            font-weight: bold;
            margin: 0;  /* Remove extra margin */
            padding: 5px 0; /* Add a little padding for spacing */
        }
        .bot-message {color: #4caf50;} /* Different color for bot messages */
        .stButton>button {background-color: #3366cc; color: white; font-size: 16px; border-radius: 8px; padding: 10px 20px; border: none; cursor: pointer;}
        .stButton>button:hover {background-color: #2850a0;}
        .sidebar .sidebar-content {background-color: #004d8c; color: grey; padding: 15px;}
        .sidebar h1 {color: #ff9800; font-size: 24px;}
        .sidebar p {font-size: 16px;}
    </style>
""", unsafe_allow_html=True)

st.write("Interact with the chatbot to get personalized learning recommendations and explanations.")






# Display the entire chat history
chat_display = "".join(st.session_state.chat_history)

# Display the chat history with proper formatting
st.markdown(f'<div class="chatbox">{chat_display}</div>', unsafe_allow_html=True)

# Add a line to scroll down after new messages are added
st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)