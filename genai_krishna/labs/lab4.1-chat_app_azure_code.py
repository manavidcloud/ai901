import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env in this folder

# All three values come from .env - change them there, not here
endpoint = os.environ["AZURE_OPENAI_BASE_URL"]
deployment_name = os.environ["CHAT_DEPLOYMENT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output_text}")
