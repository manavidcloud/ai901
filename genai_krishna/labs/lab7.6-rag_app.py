import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery 

load_dotenv()
credential = DefaultAzureCredential()          # your az login sign-in, used for both services

# Client 1: the search index
search = SearchClient(
    endpoint=os.environ["SEARCH_ENDPOINT"],
    index_name=os.environ["SEARCH_INDEX"],
    credential=credential,
)

# Client 2: the model
llm = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=get_bearer_token_provider(credential, "https://ai.azure.com/.default"),
)

question = "Which plan has the lowest deductible?"

# 1. Retrieve: hybrid search. The index embeds the question itself.
hits = search.search(
    search_text=question,
    vector_queries=[VectorizableTextQuery(text=question, k_nearest_neighbors=5, fields="text_vector")],
    select=["title", "chunk"],
    top=5,
)
sources = "\n\n".join(f"[{hit['title']}]\n{hit['chunk']}" for hit in hits)

# 2. Generate: answer only from the retrieved chunks.
response = llm.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    instructions=(
        "Answer only from the sources provided. Cite the file name in square brackets. "
        "If the sources do not contain the answer, say you do not know."
    ),
    input=f"Sources:\n{sources}\n\nQuestion: {question}",
)
print(response.output_text)