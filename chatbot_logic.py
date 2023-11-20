from openai_interface import generate_response

class Chatbot:
    def __init__(self, personality="friendly"):
        self.personality = personality

    def generate_response(self, user_input):
        return generate_response(user_input, personality=self.personality)
