# openai_interface.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(prompt, personality="friendly"):
    try:
        context_prompt = f"You are a {personality} chatbot.\nUser: {prompt}\nBot:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=context_prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded. Error: {e}")
        return "Apologies, but I'm currently limited in my responses. Please try again later."
