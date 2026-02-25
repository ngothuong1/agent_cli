from openai import OpenAI
from openai import OpenAIError
from model import OPENAI_API_KEY, MODEL_NAME, SYSTEM_PROMPT
import os

class Agent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        #Lưu lịch sử cuộc thoại
        self.history = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def run(self, user_input: str) -> str:
        #Thêm câu hỏi người dùng vào history
        self.history.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = self.client.responses.create(
                model=MODEL_NAME,
                input=self.history
            )

            output_text = response.output_text

            #Lưu câu trả lời vào history
            self.history.append({
                "role": "assistant",
                "content": output_text
            })

            return output_text
        except OpenAIError as e:
            return f"Lỗi khi gọi OpenAI: {str(e)}"