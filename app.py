import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer, MarianMTModel, MarianTokenizer

# Load the T5 model for summarization
t5_model_name = "t5-base"
summarization_model = T5ForConditionalGeneration.from_pretrained(t5_model_name)
summarization_tokenizer = T5Tokenizer.from_pretrained(t5_model_name)

# Function to get the MarianMT model name dynamically
def get_model_name(source_lang, target_lang):
    return f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

# Function for translation
def translate_text(text, source_lang, target_lang):
    model_name = get_model_name(source_lang, target_lang)
    translation_model = MarianMTModel.from_pretrained(model_name)
    translation_tokenizer = MarianTokenizer.from_pretrained(model_name)

    input_ids = translation_tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    translated_ids = translation_model.generate(input_ids, num_beams=4, max_length=100, early_stopping=True, no_repeat_ngram_size=2)
    translation = translation_tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    
    return translation

# Function for summarization
def summarize_text(text):
    input_text = "summarize: " + text
    input_ids = summarization_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    summary_ids = summarization_model.generate(input_ids, num_beams=4, max_length=50, early_stopping=True, no_repeat_ngram_size=2)
    summary = summarization_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

# Chatbot logic
def chatbot(query):
    print(f"Received query: {query}")  # Debugging: Check input
    if query.lower().startswith("summarize:"):
        text = query[len("summarize:"):].strip()
        print(f"Text to summarize: {text}")  # Debugging: Check text extraction
        return summarize_text(text)
    
    elif query.lower().startswith("translate"):
        parts = query.split(":", 1)  # Split only at the first occurrence of ":"
        
        if len(parts) == 2:
            lang_info, text = parts[0].strip(), parts[1].strip()
            print(f"Language info: {lang_info}, Text to translate: {text}")  # Debugging: Check the text and languages
            
            lang_parts = lang_info.split()
            if len(lang_parts) == 4 and lang_parts[0].lower() == "translate":
                _, source_lang, _, target_lang = lang_parts  # Now it should correctly unpack into 4 parts
                print(f"Translating from {source_lang} to {target_lang}: {text}")  # Debugging: Check language and text
                return translate_text(text, source_lang, target_lang)
            else:
                return "Please use the format: 'translate [source_lang] to [target_lang]: [text]'"
        else:
            return "Please use the format: 'translate [source_lang] to [target_lang]: [text]'"
    
    return "Please start your query with 'summarize:' or 'translate [source] to [target]:'"


# Streamlit UI setup
st.title("Chatbot for Language Processing")
st.write("This chatbot can translate text or summarize text based on your commands.")

# User input
user_input = st.text_input("Enter your request (e.g., 'summarize: Your text here' or 'translate en to fr: Your text here'):")

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter a request.")
    else:
        response = chatbot(user_input)
        st.subheader("Chatbot Response:")
        st.write(response)
