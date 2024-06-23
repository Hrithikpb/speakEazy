import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')  # Load API key from environment variables

def generate_feedback(input_text):
    try:
        # Using the ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",  # Check and use the correct model name from OpenAI
            messages=[{"role": "user", "content": input_text}],
            max_tokens=150,
            temperature=0.7  # Adjust creativity, lower values are more deterministic
        )
        feedback = response['choices'][0]['message']['content'].strip()
        return feedback
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
input_text = "You are a public speaker expert. You need to give feedback to a presentation based on posture."
f = " Feedback: The speaker's posture is good but needs to improve eye contact. Please provide detailed feedback."
feedback = generate_feedback(input_text+f)
print(feedback)