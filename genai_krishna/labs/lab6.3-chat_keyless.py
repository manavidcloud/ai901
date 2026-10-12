import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Fetches and refreshes Entra ID tokens automatically
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=token_provider,
)

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    input="Say hello in one short sentence.",
)

print(response.output_text)
