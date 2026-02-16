# 🤖 IBM Granite 4.0 Generative AI Project

This project is a beginner-friendly Generative AI application built using the **IBM Granite 4.0 h-350M model** and Hugging Face Transformers.  
The application accepts a topic from the user and generates a simple explanation in easy-to-understand language using Large Language Models (LLMs).

---

## 🚀 Project Overview

The goal of this project is to demonstrate how **Generative AI models** can be used to explain technical and non-technical topics for beginners using natural language.

The project:
- Uses **IBM Granite** as the primary model  
- Falls back to **Google FLAN-T5** if the output quality is poor  
- Cleans unwanted instructions from model responses  
- Reduces repetition using generation controls  

This makes the output more readable, beginner-friendly, and structured.

---

## ✨ Features

- Uses **IBM Granite 4.0 h-350M** open-source LLM
- Fallback support with **FLAN-T5**
- Beginner-friendly explanations
- Repetition control using `repetition_penalty`
- Regex-based output cleaning
- Structured bullet-point output
- Runs completely on **CPU (no GPU required)**

---

## 🛠 Technologies Used

- **Python**
- **Hugging Face Transformers**
- **IBM Granite 4.0 h-350M**
- **Google FLAN-T5**
- Regular Expressions (regex)

---

## 📂 Project Structure


## ⚙️ How It Works

1. The user enters a topic
2. The prompt is sent to the Granite model
3. The model generates a simple explanation
4. Output is cleaned and formatted
5. If output quality is poor, FLAN-T5 is used as a fallback

---

## ▶️ How to Run the Project

1. Clone the repository
```bash
git clone <repository-url>
cd <repository-folder>

## 🎯 **Learning Outcome**
- Understanding the basics of Generative AI
- Using pre-trained Large Language Models (LLMs)
- Prompt engineering fundamentals
- Handling noisy model outputs
- Building fallback strategies with multiple models

## 📚 **Status**
Beginner project – Created as part of learning and experimenting with Generative AI concepts.


## ✨ Project Improvements – Version 2.0

I enhanced the original Topic Explainer app with improved state management and UI features.

### 🔄 Added Features

- ✅ Topic history tracking using Streamlit session_state
- ✅ Clickable previous topics
- ✅ Clear All functionality (input, explanation, history reset)
- ✅ Improved model fallback handling (IBM Granite → FLAN-T5)
- ✅ Enhanced text cleaning using regex
- ✅ Retry mechanism for short AI outputs
- ✅ Improved UI layout using responsive column ratios

### 🧠 Technical Concepts Demonstrated

- Stateful UI management in Streamlit
- Callback functions using `on_click`
- Model caching using `@st.cache_resource`
- Text generation with Hugging Face Transformers
- Prompt engineering techniques
- Sampling parameter tuning (temperature, top_p)

This update improves both user experience and application reliability.


### 📸 Screenshots

#### 🏠 Main Interface
![Main Interface](Streamlit - 1.png)

#### 🕘 Topic History Feature
![Topic History](Streamlit - 3.png)

#### 📘 Generated Output Example
![Generated Output](Streamlit - 8.png)

### 🧹 Clear Functionality (Reset State)
![Clear Feature](Streamlit - 9.png)

## 🎥 Project Demo

A short walkthrough demonstrating:

- Topic input
- AI-generated explanations
- Topic history tracking
- Clickable topic recall
- Clear (session reset) functionality
- Model fallback system

▶️ Watch the demo below:
🔗 [Project Demo Video] (https://github.com/user-attachments/assets/4d2f4307-fa1c-4613-a033-ef097aac959d)


