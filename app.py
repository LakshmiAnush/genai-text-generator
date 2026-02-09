from transformers import pipeline
import re

# Load a free Gen AI model
generator = pipeline(
    "text2text-generation",
    model = "google/flan-t5-base"
)

print("Welcome to My First Generative AI Project!")
topic = input("Enter a topic: ")

prompt = f"Explain what is {topic} in simple words for a beginner. Write 5 simple sentences and few examples on the topic."

result = generator(
    prompt,
    max_length = 200,
    min_length = 50,
    do_sample = True,
    truncation = True
    )


output = result[0]["generated_text"]
sentences = re.findall(r'[^.!?]+[.!?]',output)

print("\nGenerted Output:\n")

for line in sentences:
   print(line.strip())
