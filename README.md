# Chatbot for Personalized Learning

Welcome to the Chatbot for Personalized Learning—an AI-driven assistant built with Rasa and powered by Hugging Face GPT-2. This chatbot provides personalized recommendations such as videos, books, and courses based on user interests and provides detailed, dynamic explanations on various topics.

## 🧠 Key Features

- **Personalized Learning Resources**: The chatbot recommends tailored learning materials, such as videos, books, and courses, based on your interests and preferred learning topics.
- **Dynamic Explanations**:It uses Hugging Face’s GPT-2 model to provide clear and detailed explanations on topics you inquire about, ensuring a rich and informative learning experience.
- **User-Friendly Interface**:The chatbot integrates Rasa for conversational interaction and Streamlit for an intuitive user interface, making learning fun and interactive.

## Requirements

- Python 3.7 or later
- Rasa Open Source
- Hugging Face Transformers library

## 🚀 Getting Started
Follow these steps to set up the chatbot on your local machine:

1. **Clone the Repository**
  Clone the repository to your local directory:
  
   ```cmd
   git clone https://github.com/your-username/personalized-learning-chatbot.git
   cd personalized-learning-chatbot

2. **Install dependencies**
   Install all the required dependencies:

   ```cmd
   pip install -r requirements.txt

3. **Train the Model**
   ```
   rasa train
   ```
Trained models are saved in models folder.

## Running the bot
Start the Rasa action server
```
rasa run actions
```
Start the rasa shell
```
rasa run -m models --enable-api --cors "*" --debug
```
Start the streamlit app
```
streamlit run app.py
```
