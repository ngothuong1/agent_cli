from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"

SYSTEM_PROMPT = """
Bạn là một AI Assistant thông minh, trả lời ngắn gon, rõ ràng và chính xác.
"""