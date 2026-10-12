import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    instructions="You are an expert AI tutor.",
    input="what is 2+2"
)

# print(f"answer: {response.output[0]}")
print(f"answer: {response.output_text}")
