from chatbot_logic import Chatbot

class UserInterface:
    def __init__(self):
        self.chatbot = Chatbot()

    def start_chat(self):
        print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break

            response = self.chatbot.generate_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    ui = UserInterface()
    ui.start_chat()
