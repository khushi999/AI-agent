from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# llm = ChatOpenAI(model = "gpt-4o-mini")
llm2 = ChatAnthropic(model = "claude-3-haiku-20240307", api_key=anthropic_api_key)
response = llm2.invoke("What is the capital of France?")
print(response)
