"""
Detect language -> redact PII -> translate to English + summarise (single file).
This is a PIPELINE (fixed steps in code), not an agent.

Setup (once):
    pip install azure-ai-textanalytics azure-ai-projects azure-identity openai
    az login
Run:
    python 12d_translate_pii_pipeline.py
"""
from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.projects import AIProjectClient

# ---- change these 3 values ----
LANG_ENDPOINT    = "https://<FOUNDRY_NAME>.cognitiveservices.azure.com/"
PROJECT_ENDPOINT = "https://<FOUNDRY_NAME>.services.ai.azure.com/api/projects/<PROJECT>"
MODEL            = "gpt-5-mini"   # your deployment name

cred = DefaultAzureCredential()   # uses az login, no keys
lang_client = TextAnalyticsClient(LANG_ENDPOINT, cred)
llm = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=cred).get_openai_client()

messages = [
    "Bonjour, je m'appelle Marie Dupont, mon numéro est 06 12 34 56 78. Ma commande est en retard.",
    "Hola, soy Carlos García, mi correo es carlos@example.com. Me cobraron dos veces.",
]

for msg in messages:
    # 1. detect language (Language API - tool)
    lang = lang_client.detect_language([msg])[0].primary_language

    # 2. redact PII in that language (Language API - tool)
    pii = lang_client.recognize_pii_entities([msg], language=lang.iso6391_name)[0]

    # 3. LLM translates + summarises ONLY the redacted text
    resp = llm.responses.create(
        model=MODEL,
        instructions="Translate the text to English, keep the **** masks as-is, "
                     "then add: Summary, Category, Priority.",
        input=pii.redacted_text,
    )

    print("Language   :", lang.name, f"({lang.iso6391_name})")
    print("PII found  :", [(e.category, e.text) for e in pii.entities])
    print("Sent to LLM:", pii.redacted_text)
    print("LLM reply  :\n", resp.output_text, "\n" + "-" * 60)
