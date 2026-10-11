import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                                   # reads .env

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],        # deployment name, not model name
    instructions="You are an expert AI tutor.", # Custom prompt to model
    input="Explain the role of Azure Private Endpoints in securing LLM deployments.",
    reasoning={"effort": "low"},
    text={"verbosity": "low"},
    max_output_tokens=1000,
)

print(response.output_text)