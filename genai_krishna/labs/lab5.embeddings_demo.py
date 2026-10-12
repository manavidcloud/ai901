import os
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

docs = [
    "Microsoft Azure provides enterprise security for Generative AI.",
    "Cloud platforms offer robust safety for artificial intelligence workloads.",
    "Panthers hunt prey in the African savanna.",
]

# One call embeds all three texts
result = client.embeddings.create(model=os.environ["EMBEDDING_DEPLOYMENT"], input=docs)
vectors = [np.array(item.embedding) for item in result.data]

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

print(f"Dimensions: {len(vectors[0])}")
print(f"Doc 1 vs Doc 2 (same topic): {cosine(vectors[0], vectors[1]):.4f}")
print(f"Doc 1 vs Doc 3 (unrelated):  {cosine(vectors[0], vectors[2]):.4f}")