# Intelligent Chatbot for Text Summarization and Translation

This project involves the development of an intelligent chatbot that can summarize and translate text. Powered by **Large Language Models (LLMs)**, the chatbot provides an efficient solution for text summarization and translation tasks using advanced **Natural Language Processing (NLP)** techniques.

---

## Features

- **Text Summarization:** Summarize long and complex texts into concise versions.
- **Language Translation:** Translate text between multiple languages, including **English**, **French**, and **Spanish**.
- **Conversational Interface:** The chatbot greets users and guides them in choosing whether they want a text summary or a translation.
- **Support for Long Texts:** Handles both short phrases and long, detailed texts.

---

## Technologies

- **Large Language Models (LLMs)** for advanced NLP tasks (e.g., MarianMT, T5)
- **Python** for backend logic
  - Flask or Streamlit for web-based deployment
- **Hugging Face Transformers** for pre-trained models
- **Natural Language Processing (NLP)** libraries: 
  - `transformers`
  - `torch`
  - `nltk`
  
---

## Installation

### Requirements

- Python 3.x

### Steps

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/nihelzaied13/Intelligent-Chatbot-for-Text-Summarization-and-Translation.git
   ```

2.   Navigate to the project directory:

```bash
cd Chatbot for translation and summarization
```
3.Create a virtual environment:

```bash
python -m venv chatbot_t5
```

4.Activate the virtual environment:
```bash
conda activate chatbot_t5
```

### Usage :
To run the chatbot locally, use the following command:

```bash
streamlit run app.py
```

### How to Use
Summarization:

Enter the text you want to summarize.
The chatbot will return a concise version of the text.

Translation:
Specify the source and target languages.
The chatbot will translate the text accordingly.

Example inputs:
Summarize: summarize: This is a long text that needs to be summarized.
Translate: translate en to es: How are you?





   
