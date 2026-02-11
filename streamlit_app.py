import streamlit as st
from transformers import pipeline
import re

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="Generative AI Text Generator", layout="centered")
st.title("🤖 My First Generative AI Project : Topic Explainer")
st.write("This app generates simple explanations using IBM Granite model with Google FLAN-T5 as fallback.")

# -------------------------------
# Load models (cached)
# -------------------------------
@st.cache_resource
def load_model():
    try:
        # Attempt IBM Granite (may fail if no license)
        model = pipeline(
            "text-generation",
            model="ibm-granite/granite-4.0-h-350M",
            trust_remote_code=True
        )
        return model, "granite"
    except Exception:
        st.warning("Granite model unavailable. Using Google FLAN-T5 as fallback.")
        model = pipeline(
            "text2text-generation",
            model="google/flan-t5-large"
        )
        return model, "flan"

generator, model_type = load_model()
st.caption(f"🧠 Model in use: {model_type.upper()}")

# -------------------------------
# Clean output
# -------------------------------
def clean_output(text):
    patterns = [
        r"(?i)^you are.*",
        r"(?i)^topic:.*",
        r"(?i)^provide.*",
        r"(?i)^write.*",
        r"(?i)^i will explain.*",
        r"(?i)^define.*",
        r"(?i)^here are.*",
        r"(?i)^answer.*",
        r"(?i)^explain.*",
        r"(?i)^what is.*",
        r"(?i)^the answer should.*",
        r"(?i)^answer the following.*",
        r".*\?\s*$",
        r"\*{2,}",
        r"-{2,}",
        r"^\s*-\s*",
        r"['\"]",
        r"(?m)^#.*"
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    # Remove duplicate paragraphs
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    unique_paragraphs = list(dict.fromkeys(paragraphs))

    return "\n".join(unique_paragraphs).strip()

# -------------------------------
# Initialize session state
# -------------------------------
if "topic_input" not in st.session_state:
    st.session_state.topic_input = ""


# -------------------------------
# User Input Form
# -------------------------------
with st.form(key="topic_form"):
    st.session_state.topic_input = st.text_input("Enter a topic:")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        submit_button = st.form_submit_button("Generate Explanation")
    with col3:
        clear_button = st.form_submit_button("Clear Explanation")

# -------------------------------
# Clear Topic
# -------------------------------
if clear_button:
    st.session_state.topic_input = ""
    st.stop()  # Rerun app to clear input box

# -------------------------------
# Generate Explanation
# -------------------------------
if submit_button:
    topic = st.session_state.topic_input.strip()
    if not topic:
        st.warning("Please enter a topic.")
    else:
        prompt = f"Explain {topic} in simple words for a beginner. Write at least 5 sentences."

        with st.spinner("Generating explanation..."):
            try:
                if model_type == "granite":
                    result = generator(
                        prompt,
                        max_new_tokens=300,
                        temperature=0.7,
                        top_p=0.9,
                        do_sample=True,
                        repetition_penalty = 1.2,
                        return_full_text=False
                    )
                else:
                    result = generator(
                        prompt,
                        max_length=400
                    )

                output_text = clean_output(result[0]["generated_text"])

                # Retry if output too short
                if len(output_text.split()) < 25 and model_type == "granite":
                    retry = generator(
                        prompt,
                        max_new_tokens=300,
                        temperature=0.9,
                        do_sample=True,
                        return_full_text=False
                    )
                    output_text = clean_output(retry[0]["generated_text"])

            except Exception as e:
                st.error("Model failed to generate response.")
                st.stop()

        # -------------------------------
        # Display output
        # -------------------------------
        st.subheader("📘 Generated Explanation")
        if output_text:
            sentences = re.split(r'(?<=[.!?])\s+', output_text)
            for sentence in sentences:
                st.write(sentence.strip())
        else:
            st.write("No explanation generated. Try a different topic.")