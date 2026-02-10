"""
Generative AI Mini-Project: IBM Granite + Google FLAN-T5
Author: Lakshmi M B
Purpose: Generate beginner-friendly explanations for a given topic.
Models:
- IBM Granite (demo, CPU may be slow)
- Google FLAN-T5 (fallback, reliable on CPU)
"""


from transformers import pipeline
import re

# -------------------------------
# Load models
# -------------------------------

# IBM Granite (demo model)
granite_generator = pipeline(
    "text-generation",
    model="ibm-granite/granite-4.0-h-350M",
    trust_remote_code=True
)

# Google FLAN-T5 (fallback model)
flan_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

# -------------------------------
# Helper function to clean output
# -------------------------------

def clean_output(text):
    """
    Removes instruction-like lines and junk patterns
    """
    bad_words = [
        r"(?i)^explain.*",
        r"(?i)^describe.*",
        r"(?i)^write.*",
        r"(?i)^do not.*",
        r"(?i)^include.*",
        r"(?i)^in your answer.*",
        r"(?i)^here is.*",
        r"(?i)^answer:.*",
        r"['\"]",
        r"\*{2,}",     # ** markdown
        r"-{2,}"       # ---
    ]

    for word in bad_words:
        text = re.sub(word, "", text, flags=re.MULTILINE)

    return text.strip()

# -------------------------------
# User input
# -------------------------------

print("Welcome to My First Generative AI Project!")
topic = input("Enter a topic: ").strip()

# Simple, safe prompt (VERY important)
prompt = f"""Explain {topic} in simple words for a beginner.
Write atleast 5 complete sentences.
"""

print("\nGenerating output...\n")

# -------------------------------
# Try Granite first
# -------------------------------

granite_output = ""

try:
    result = granite_generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        repetition_penalty = 1.2,
        return_full_text=False
    )
    granite_output = result[0]["generated_text"]
    granite_output = clean_output(granite_output)

except Exception as e:
    granite_output = ""

# -------------------------------
# Decide fallback
# -------------------------------

# If Granite output is too short or bad → use FLAN
if not granite_output or len(granite_output.split()) < 40:
    flan_result = flan_generator(
        prompt,
        max_length=500,
        do_sample=True,
        temperature=0.7
    )
    output_text = clean_output(flan_result[0]["generated_text"])
else:
    output_text = granite_output

# -------------------------------
# Sentence formatting
# -------------------------------

sentences = re.findall(r'[^.!?]+[.!?]', output_text)

print("Structured Output:\n")


for s in sentences:
    s = s.strip()
    if len(s) >= 25:
        print(f"• {s}")