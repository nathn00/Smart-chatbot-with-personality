## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# 인격을 가진 스마트 챗봇
### Feat. OpenAI GPT API

## 프로젝트 설명:

 해당 프로젝트는 OpenAI GPT-3 API를 활용한 인공지능(AI) 챗봇입니다! 
 사용자의 입력에 응답하며, 사용자에게 다양한 주제에 관한 정보를 제공하거나 간단한 대화를 할 수 있습니다. 
 프로젝트는 여러 파일로 구성되어 있으며, 각 파일은 아래와 같은 특정 역할을 담당합니다.

## 파일 설명:

### 1. `config.py`

OpenAI API 키를 저장하여 GPT API에 접근할 수 있게 합니다.

```python
OPENAI_API_KEY = "openai_api_key"
# 저의 AIP_KEY는 횟수제한이 초과되어 교수님의 OpenAI API KEY로 대체하여 테스트 해주시면 감사하겠습니다...!
# 해당 파일은 보안 문제로 .gitignore에 추가하였습니다. 
```

### 2. `openai_interface.py`
OpenAI API와 상호작용하며 챗봇의 응답을 생성하는 함수를 제공합니다.
API 호출 제한을 예상하여 에러처리를 합니다.
```python
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(prompt, personality="friendly"):
        prompt = f"You are a {personality} chatbot. User: {prompt}\nBot:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        # Handle rate limit error gracefully
        print(f"Rate limit exceeded. Error: {e}")
        return "Apologies, but I'm currently limited in my responses. Please try again later."
```

3. `chatbot_logic.py`
Chatbot 클래스를 정의하고, 챗봇의 성격과 OpenAI 인터페이스를 사용하여 응답을 생성하는 메서드를 포함하고 있습니다.
```python
from openai_interface import generate_response

class Chatbot:
    def __init__(self, personality="friendly"):
        self.personality = personality

    def generate_response(self, user_input):
        return generate_response(user_input, personality=self.personality)
```

4. `user_interface.py`
사용자와 챗봇 간의 상호작용을 관리하는 클래스로, 
대화를 시작하고 유자하는 사용자 인터페이스를 제공합니다.
```python
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
```

5. `main.py`
프로그램의 시작 함수입니다.
파일을 실행하여 대화를 시작합니다.
```python
from user_interface import UserInterface

if __name__ == "__main__":
    ui = UserInterface()
    ui.start_chat()
``` 

## Testing Program
![Screenshot 2023-11-20 at 14 58 15](https://github.com/nathn00/nathn00/assets/89184540/6b594b57-faf3-4107-9f94-d8d9f895c1cc)

```text
사용 방법:
OpenAI API 키 설정: config.py을 만들고 OPENAI_API_KEY = "openai_api_key"에 OPENAI_API_KEY키를 삽입해주세요.
프로그램 실행: main.py를 실행하여 챗봇과 대화를 시작하세요

주의 사항:
코드에는 OpenAI API 오류를 처리하는 기능이 포함되어 있습니다.
보안상 문제로 config.py는 올려두지 않았으니 위의 사항 반영하여 실행시켜 주시면 감사하겠습니다!
```
해당 <a href="https://techbukket.com/blog/openai-function-python">블로그</a>를 참고하여 함수를 작성했습니다.