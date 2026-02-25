from service import Agent
from dotenv import load_dotenv
import os

load_dotenv()
print ("DEBUG ENV PATH:", os.getcwd())
print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))

def main():
    print("---AGENT CLI---")
    print("Gõ 'exit' để thoát.\n")

    agent = Agent()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Tạm biệt")
            break

        response = agent.run(user_input)
        print("AI:", response)
        print()

if __name__ == "__main__":
    main()