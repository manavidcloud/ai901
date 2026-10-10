# Generative AI on Azure: Azure OpenAI in Microsoft Foundry (Hands-On Guide)

## Lab Index

Click a lab to jump to it. Every section has a **⬆ Back to Lab Index** link under its heading.

| Lab | What you do | Where | Python? | Extra cost |
| :--- | :--- | :--- | :---: | :--- |
| [**Lab 1: Create the Foundry Resource and Project**](#4-lab-1-create-the-foundry-resource-and-project) | Create the resource, find endpoint and key | Azure portal, Foundry portal | No | None |
| [**Lab 2: Deploy a Chat Model and an Embedding Model**](#5-lab-2-deploy-a-chat-model-and-an-embedding-model) | Deploy `gpt-5.4-mini` and `text-embedding-3-small` | Foundry portal | No | None until used |
| [**Lab 3: Test in the Playground and Tune Parameters**](#7-lab-3-test-in-the-playground-and-tune-parameters) | Chat with the model, change settings | Foundry portal | No | Tokens |
| [**Lab 4: Call the Model from Python**](#8-lab-4-call-the-model-from-python) | First script, multi-turn chat, streaming | Your machine | Yes | Tokens |
| [**Lab 5: Embeddings and Semantic Similarity**](#9-lab-5-embeddings-and-semantic-similarity) | Turn text into vectors and compare them | Your machine | Yes | Tokens |
| [**Lab 6: Keyless Authentication with Microsoft Entra ID**](#10-lab-6-keyless-authentication-with-microsoft-entra-id) | Assign a role, call the model with no key | Azure portal, your machine | Yes | None |
| [**Lab 7: RAG with Azure AI Search**](#11-lab-7-rag-with-azure-ai-search) | Index your PDFs and ask questions about them | Azure portal, your machine | Yes | **AI Search Basic, hourly** |
| [**Lab 8: Network Isolation with Private Endpoints**](#12-lab-8-network-isolation-with-private-endpoints) | Remove public access to the endpoint | Azure portal | No | Private endpoint, hourly |
| [**Lab 9: Guardrails and Content Safety**](#13-lab-9-guardrails-and-content-safety) | Create, assign and test a guardrail | Foundry portal | No | None |
| [**Lab 10: Cost Control and Clean-Up**](#14-lab-10-cost-control-and-clean-up) | Budget alert, usage, delete everything | Azure portal | No | None |
| [**Lab 11: Prompt Engineering**](#15-lab-11-prompt-engineering) | Write prompts that give reliable answers | Foundry portal, your machine | A little | Tokens |
| [**Lab 12: Structured Outputs (JSON)**](#16-lab-12-structured-outputs-json) | Get JSON that always matches your schema | Your machine | Yes | Tokens |
| [**Lab 13: Function Calling**](#17-lab-13-function-calling) | Let the model call your Python function | Your machine | Yes | Tokens |

**Suggested order:** Labs 1 to 5, then 11 to 13, then 6, 7 and 9. Do Lab 8 near the end because it blocks access from your machine, and finish with the clean-up in Lab 10.

### Concepts and reference

| Section | Read it for |
| :--- | :--- |
| [1. Core Concepts](#1-core-concepts) | Tokens, context window, embeddings, RAG in plain words |
| [2. OpenAI API vs. Azure OpenAI in Microsoft Foundry](#2-openai-api-vs-azure-openai-in-microsoft-foundry) | Why a company picks Azure |
| [3. How Azure Organises It](#3-how-azure-organises-it-resource-project-deployment) | Resource, project, deployment, and the two portals |
| [6. Models, Deployment Types and Model Lifecycle](#6-models-deployment-types-and-model-lifecycle) | Which model to pick, where data is processed, retirement |
| [18. Troubleshooting](#18-troubleshooting) | What an error code means and how to fix it |
| [Reference Links](#reference-links) | The Microsoft Learn pages behind each lab |

---

**Names used in every lab** (change them once here and reuse):

| Thing | Value used in this guide |
| :--- | :--- |
| Resource group | `rg-genai-lab` |
| Region | `eastus2` (any region that offers your model works) |
| Foundry resource | `foundry-genai-lab-<yourname>` (must be globally unique) |
| Project | `genai-lab-project` |
| Chat deployment | `gpt-5.4-mini` |
| Embedding deployment | `text-embedding-3-small` |

---

## 1. Core Concepts

[⬆ Back to Lab Index](#lab-index)

* **Generative AI:** models that produce new text, images, code, audio or video from patterns learned in training.
* **Foundation model:** a large model trained on broad data that can be used for many tasks without retraining.
* **Large Language Model (LLM):** a foundation model for understanding and generating language. Current GPT models also accept images as input.
* **Reasoning model:** a model that "thinks" before it answers. The thinking uses hidden *reasoning tokens*, which you pay for as output tokens. All current GPT-5.x and GPT-6 models are reasoning models.
* **Token:** the unit a model reads and writes. Roughly, 1,000 tokens is about 750 English words. You are billed per token.
* **Context window:** the most tokens one request can hold, counting instructions, history, retrieved documents and the answer.
* **Embedding:** a list of numbers that represents the meaning of a text, so that similar texts have similar numbers.
* **RAG (Retrieval-Augmented Generation):** look up relevant chunks of your own documents first, then give them to the model with the question.

---

## 2. OpenAI API vs. Azure OpenAI in Microsoft Foundry

[⬆ Back to Lab Index](#lab-index)

The models are the same. The difference is where they run and how you control access.

| Dimension | OpenAI API | Azure OpenAI in Microsoft Foundry |
| :--- | :--- | :--- |
| **Hosting** | OpenAI's platform | Microsoft Azure regions, inside your subscription |
| **Your data** | OpenAI API data terms | Prompts and outputs are not used to train models and are not shared with OpenAI |
| **Authentication** | API keys | API keys or Microsoft Entra ID with Azure RBAC |
| **Network** | Public endpoint | Public, selected networks, or private endpoints only |
| **Data residency** | Limited choice | Choose Global, Data Zone (US / EU / APAC) or a single geography |
| **Compliance** | OpenAI's certifications | Azure compliance portfolio (ISO, SOC, HIPAA and others) |
| **Billing** | OpenAI account | Your Azure subscription, with budgets and cost alerts |
| **Other models** | OpenAI models only | Same endpoint also serves Claude, Grok, DeepSeek, Llama, Mistral and Phi models |

---

## 3. How Azure Organises It: Resource, Project, Deployment

[⬆ Back to Lab Index](#lab-index)

```
Azure subscription
└── Resource group: rg-genai-lab
    └── Foundry resource: foundry-genai-lab-<yourname>      (kind: AIServices)
        │   Holds: endpoint, keys, networking, identity, billing
        │
        ├── Project: genai-lab-project                      (groups your work)
        │
        ├── Deployment: gpt-5.4-mini            → model gpt-5.4-mini (2026-03-17)
        └── Deployment: text-embedding-3-small  → model text-embedding-3-small (1)
```

* **Foundry resource:** the Azure resource you create. It gives you one endpoint and one set of keys for Azure OpenAI and the other Foundry tools.
* **Project:** a workspace inside the resource for models, agents and evaluations.
* **Deployment:** a model made callable under a name you choose. Your code sends the **deployment name** in the `model` field, not the underlying model name. Keeping the two identical is fine for learning.

You work in two portals:

| Portal | URL | Use it for |
| :--- | :--- | :--- |
| **Azure portal** | https://portal.azure.com | Create the resource, keys, access control (IAM), networking, cost, delete |
| **Microsoft Foundry portal** | https://ai.azure.com | Projects, deploy models, playground, guardrails |

---

## 4. Lab 1: Create the Foundry Resource and Project

[⬆ Back to Lab Index](#lab-index)

**You need:** an Azure subscription and the **Owner** role on it (or on the resource group). Owner is needed later to assign roles. No access request form is needed for the models used here.

### Option A: Foundry portal (fastest, creates resource and project together)

1. Open https://ai.azure.com and sign in.
2. Make sure the **New Foundry** toggle at the top is **on**.
3. First visit: in the project dropdown select **Create a new project**. Otherwise: select the project name in the upper-left corner, then **Create new project**.
4. **Project name:** `genai-lab-project`.
5. Select **Advanced options**:
   * **Resource group:** create new → `rg-genai-lab`.
   * **Location:** `East US 2`.
6. Select **Create project** and wait for the project overview page.

### Option B: Azure portal (more control over network, identity and tags)

1. Open the create page directly: https://portal.azure.com/#create/Microsoft.CognitiveServicesAIFoundry
   (or search the top bar for **Microsoft Foundry** → **Create**).
2. On the **Basics** tab fill in:
   * **Subscription:** your subscription.
   * **Resource group:** **Create new** → `rg-genai-lab`.
   * **Region:** `East US 2`.
   * **Name:** `foundry-genai-lab-<yourname>`.
3. Leave **Network** on **All networks** for now (Lab 8 locks it down). Leave **Identity**, **Encryption** and **Storage** on defaults.
4. Select **Review + create**, then **Create**.
5. When deployment finishes select **Go to resource**. On the **Overview** page check **Status** is available.
6. Open the Foundry portal (https://ai.azure.com), pick this resource, and create the project `genai-lab-project` if one was not created for you.

<details>
<summary>▶ Azure CLI: create resource group, Foundry resource and project</summary>

Needs Azure CLI 2.80.0 or later (`az version`, then `az upgrade` if older).

```bash
az login

az group create --name rg-genai-lab --location eastus2

# --custom-domain must be globally unique. --allow-project-management cannot be changed later.
az cognitiveservices account create \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --kind AIServices \
    --sku S0 \
    --location eastus2 \
    --custom-domain foundry-genai-lab-<yourname> \
    --assign-identity \
    --allow-project-management true

az cognitiveservices account project create \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --project-name genai-lab-project \
    --location eastus2

# Should print: Succeeded
az cognitiveservices account show \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --query properties.provisioningState --output tsv
```

</details>

### Find your endpoint and key

1. In the **Azure portal**, open the resource `foundry-genai-lab-<yourname>`.
2. In the left menu select **Resource Management** → **Keys and Endpoint**.
3. Copy **KEY 1** and the endpoint. You use them in Lab 4.

<details>
<summary>▶ Azure CLI: show endpoint and key</summary>

```bash
az cognitiveservices account show \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --query properties.endpoint --output tsv

az cognitiveservices account keys list \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --query key1 --output tsv
```

</details>

---

## 5. Lab 2: Deploy a Chat Model and an Embedding Model

[⬆ Back to Lab Index](#lab-index)

### Deploy the chat model

1. In the **Foundry portal**, open `genai-lab-project`.
2. Select **Build** in the upper-right navigation, then **Models** in the left pane.
3. Select **Deploy** → **Deploy a base model**.
4. Search for **gpt-5.4-mini** and select it.
5. Select **Deploy** → **Default settings**. (Choose **Custom settings** if you want to change the deployment name, deployment type or tokens-per-minute limit.)
6. The portal opens the playground when the deployment succeeds. Note the deployment name: `gpt-5.4-mini`.

### Deploy the embedding model

Repeat steps 2 to 5 and search for **text-embedding-3-small**. Note the deployment name.

### Check both deployments

**Build** → **Models** lists your deployments. Both should show **Succeeded**. Select a deployment to see its endpoint details and keys, change its settings, or delete it.

<details>
<summary>▶ Azure CLI: list models in a region, deploy, verify</summary>

```bash
# Which versions and deployment types does my region offer?
az cognitiveservices model list \
    --location eastus2 \
    --query "[?model.name=='gpt-5.4-mini'].{version:model.version,skus:join(',',model.skus[].name)}" \
    --output table

# Chat model. --sku-capacity is the rate limit in thousands of tokens per minute.
az cognitiveservices account deployment create \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --deployment-name gpt-5.4-mini \
    --model-name gpt-5.4-mini \
    --model-version "2026-03-17" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name GlobalStandard

# Embedding model
az cognitiveservices account deployment create \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --deployment-name text-embedding-3-small \
    --model-name text-embedding-3-small \
    --model-version "1" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name GlobalStandard

# Should print: Succeeded
az cognitiveservices account deployment show \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --deployment-name gpt-5.4-mini \
    --query properties.provisioningState --output tsv
```

If a command fails with `DeploymentModelNotSupported`, that model, version or SKU is not offered in your region. Use the output of the first command to pick a combination that is.

</details>

---

## 6. Models, Deployment Types and Model Lifecycle

[⬆ Back to Lab Index](#lab-index)

### Azure OpenAI models you can deploy (October 2026)

| Family | Model IDs | Use it for | Context window |
| :--- | :--- | :--- | :--- |
| **GPT-6.1 / GPT-6** | `gpt-6.1-sol`, `gpt-6-sol`, `gpt-6-astra`, `gpt-6-luna` | Hardest reasoning, long agentic work | 1,050,000 (128,000 output) |
| **GPT-5.6** | `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna` | Flagship general work. GA until Jan 2028 | 1,050,000 (128,000 output) |
| **GPT-5.5 / GPT-5.4** | `gpt-5.5`, `gpt-5.4`, `gpt-5.4-pro` | Strong general reasoning | 1,050,000 (128,000 output) |
| **GPT-5.4 small** | `gpt-5.4-mini`, `gpt-5.4-nano` | **Learning, high volume, low cost.** GA until Sep 2027 | 400,000 (128,000 output) |
| **Coding** | `gpt-5.3-codex`, `gpt-5.2-codex` | Code generation and agents (Responses API only) | 400,000 |
| **Embeddings** | `text-embedding-3-small` (1,536 dims), `text-embedding-3-large` (3,072 dims) | Vector search and RAG. GA until Feb 2028 | 8,192 input |
| **Images** | `gpt-image-2`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | Image generation and editing | n/a |
| **Audio** | `gpt-realtime-2.1`, `gpt-realtime-2.1-mini`, `gpt-audio-1.5`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-tts` | Voice agents, speech-to-text, text-to-speech | n/a |
| **Video** | `sora-2` (preview) | Video generation | n/a |
| **Routing** | `model-router` | Sends each prompt to a suitable model automatically | n/a |

Notes:

* GPT-5.6 and GPT-6 need a quota request on lower quota tiers. `gpt-5.4-mini` deploys with default quota, which is why the labs use it.
* You cannot switch embedding models on an existing index. Changing model means re-embedding every document.
* The same Foundry resource also deploys models from Anthropic (Claude), xAI (Grok), DeepSeek, Meta (Llama), Mistral and Microsoft (Phi). Models from partners need an Azure Marketplace subscription step during deployment.

### Deployment types

| Deployment type | SKU code | Where data is processed | Billing | Best for |
| :--- | :--- | :--- | :--- | :--- |
| **Global Standard** | `GlobalStandard` | Any Azure region | Pay per token | **Default choice.** New models arrive here first |
| **Data Zone Standard** | `DataZoneStandard` | Inside US, EU or APAC zone | Pay per token | Data-zone compliance |
| **Standard** | `Standard` | Inside one Azure geography | Pay per token | Strict geography rules, low volume |
| **Global / Data Zone / Regional Provisioned** | `GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, `ProvisionedManaged` | Global, zone or geography | Reserved PTUs | Steady high volume, low latency variance |
| **Global / Data Zone Batch** | `GlobalBatch`, `DataZoneBatch` | Global or zone | 50% cheaper, 24-hour target | Large jobs that can wait |
| **Developer** | `DeveloperTier` | Any Azure region | Pay per token | Testing a fine-tuned model (24-hour lifetime, no SLA) |

Data **at rest** always stays in the geography of your resource. The deployment type only decides where **inference** runs.

### Model lifecycle

Models do not live forever. Plan for it.

| Stage | Meaning |
| :--- | :--- |
| **Preview** | Experimental. Can change or disappear with 30 days' notice |
| **Generally Available (GA)** | Production-ready. Retirement date is set at launch, normally 18 months out |
| **Legacy / Deprecated** | Newer models exist. From month 12, new customers can no longer deploy it |
| **Retired** | Removed. Every call returns `410 Gone` |

* Standard, Data Zone Standard and Global Standard deployments are **upgraded automatically** to the replacement model at retirement. Provisioned deployments are not; you migrate them yourself.
* Each deployment has a version upgrade policy: upgrade when a new default appears, upgrade only at retirement, or never upgrade (then it stops working at retirement).
* Azure emails subscription owners at least 60 days before a GA model retires.

<details>
<summary>▶ Azure CLI: check lifecycle status and retirement dates for a model</summary>

```bash
az cognitiveservices model list \
    --location eastus2 \
    --query "[?model.name=='gpt-5.4-mini'].{version:model.version,status:model.lifecycleStatus,retires:model.deprecation.inference}" \
    --output table
```

In this output `Deprecating` means deprecated (still works) and `Deprecated` means retired.

</details>

---

## 7. Lab 3: Test in the Playground and Tune Parameters

[⬆ Back to Lab Index](#lab-index)

1. In the **Foundry portal** select **Build** → **Models**.
2. Select the **gpt-5.4-mini** deployment. The chat playground opens.
3. Put a persona in the instructions box, for example: `You are an expert AI tutor. Answer in under 120 words.`
4. Type a prompt and send it.
5. Change one setting at a time and resend to see its effect.
6. Select the **Code** tab to get a ready-made code sample for exactly what you just ran.

### Parameter reference

| Parameter | What it does | Typical values |
| :--- | :--- | :--- |
| **Instructions** (`instructions`) | Rules, persona and output format. Sent as a *developer* message, which works the same as a system message. Send one or the other, not both | Short, specific rules |
| **Reasoning effort** (`reasoning.effort`) | How long the model thinks before answering. More effort means better answers on hard problems, more latency and more cost | `none`, `minimal`, `low`, `medium`, `high`, `xhigh` (supported values vary by model) |
| **Verbosity** (`text.verbosity`) | How long and detailed the visible answer is | `low`, `medium`, `high` |
| **Max output tokens** (`max_output_tokens`) | Hard cap on reasoning tokens plus visible answer. Too low and the answer is cut off or empty | 1,000 or more with reasoning on |
| **Temperature** (`temperature`) | Randomness. Low is repeatable and factual, high is varied and creative | 0.0 to 2.0 |
| **Top P** (`top_p`) | Sample only from the most likely tokens that add up to probability P. Change temperature or top P, not both | 0.0 to 1.0 |
| **Structured output** (`text.format`) | Forces the answer to match a JSON schema | A JSON schema |

Temperature and top P are accepted by GPT-6 models. Other reasoning models may reject them with an "unsupported parameter" error; if so, remove them and steer with reasoning effort and verbosity instead.

---

## 8. Lab 4: Call the Model from Python

[⬆ Back to Lab Index](#lab-index)

Azure OpenAI uses the **v1 API**: the standard `openai` package, the standard `OpenAI()` client, and a base URL that ends in `/openai/v1/`. There is no `api-version` to manage. The recommended call is the **Responses API** (`client.responses.create`).

### Install

```bash
pip install openai python-dotenv
```

### `.env` (this is the only file you change)

```env
# Endpoint from Lab 1 + /openai/v1/
AZURE_OPENAI_BASE_URL="https://foundry-genai-lab-<yourname>.openai.azure.com/openai/v1/"
AZURE_OPENAI_API_KEY="paste-KEY-1-here"
# Deployment names from Lab 2
CHAT_DEPLOYMENT="gpt-5.4-mini"
EMBEDDING_DEPLOYMENT="text-embedding-3-small"
```

Add `.env` to `.gitignore`. Never commit a key.

### `chat_app.py`

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],        # deployment name, not model name
    instructions="You are an expert AI tutor.",
    input="Explain the role of Azure Private Endpoints in securing LLM deployments.",
    reasoning={"effort": "low"},
    text={"verbosity": "low"},
    max_output_tokens=1000,
)

print(response.output_text)
```

Run it with `python chat_app.py`.

### Keep a conversation going

The service stores each response for 30 days, so a follow-up only needs the previous response ID.

```python
follow_up = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    previous_response_id=response.id,
    input="Now explain it to a college freshman.",
)
print(follow_up.output_text)
```

### Stream the answer as it is generated

```python
stream = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    input="Summarise Azure OpenAI in one sentence.",
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")
```

### What else the Responses API does

* **Structured outputs:** JSON that always matches your schema, set through `text.format`. See [Lab 12](#16-lab-12-structured-outputs-json).
* **Function calling:** the model asks your code to run a function and uses the result. See [Lab 13](#17-lab-13-function-calling).
* **Built-in tools:** code interpreter, image generation, remote MCP servers.
* **Background mode:** long tasks that run asynchronously.

The Chat Completions API (`client.chat.completions.create`) still works on the same client and is what models from other providers on Foundry use.

<details>
<summary>▶ curl: the same call with no SDK</summary>

```bash
curl -X POST "https://foundry-genai-lab-<yourname>.openai.azure.com/openai/v1/responses" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
     "model": "gpt-5.4-mini",
     "input": "This is a test."
    }'
```

</details>

---

## 9. Lab 5: Embeddings and Semantic Similarity

[⬆ Back to Lab Index](#lab-index)

An embedding turns text into a vector. Two texts with close meaning give vectors that point in nearly the same direction, which cosine similarity measures (1.0 is identical direction, near 0 is unrelated).

```bash
pip install numpy
```

### `embeddings_demo.py`

```python
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
```

Expected: 1,536 dimensions, and a clearly higher score for the first pair.

---

## 10. Lab 6: Keyless Authentication with Microsoft Entra ID

[⬆ Back to Lab Index](#lab-index)

An API key is a shared password: anyone who copies it can call your model and you cannot tell who did. With Entra ID, each user or app signs in as itself and Azure RBAC decides what it may do. Use keys for a quick test and Entra ID for everything else.

### Step 1: Give yourself the role (Azure portal)

1. Open the Foundry resource in the **Azure portal**.
2. Select **Access control (IAM)** → **+ Add** → **Add role assignment**.
3. On the **Role** tab search for **Cognitive Services OpenAI User**, select it, then **Next**.
4. On the **Members** tab keep **User, group, or service principal**, choose **+ Select members**, pick your own account, then **Select**.
5. Select **Review + assign** twice. Role changes can take a few minutes to apply.

<details>
<summary>▶ Azure CLI: assign the role</summary>

```bash
RESOURCE_ID=$(az cognitiveservices account show \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --query id --output tsv)

az role assignment create \
    --role "Cognitive Services OpenAI User" \
    --assignee "you@yourdomain.com" \
    --scope $RESOURCE_ID
```

</details>

### Step 2: Sign in locally

```bash
az login
pip install azure-identity
```

### Step 3: `chat_keyless.py`

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

# Fetches and refreshes Entra ID tokens automatically
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=token_provider,                      # no key in the code or in .env
)

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    input="Say hello in one short sentence.",
)
print(response.output_text)
```

`DefaultAzureCredential` uses your `az login` on a laptop and a **managed identity** when the same code runs on Azure (App Service, Container Apps, AKS, Functions). For an app on Azure, turn on its managed identity under **Identity** → **System assigned** → **On**, then repeat Step 1 with **Managed identity** as the member type.

### Roles worth knowing

| Role | Allows |
| :--- | :--- |
| **Cognitive Services OpenAI User** | Call deployed models. Least privilege for an app |
| **Cognitive Services Contributor** | Create and manage deployments |
| **Foundry User** | Build and test inside a Foundry project |
| **Foundry Project Manager** | Foundry User plus manage the project and invite users |
| **Foundry Account Owner** | Manage the resource and projects, create guardrails |
| **Owner / Contributor** | Manage the Azure resource only. These do **not** include permission to call models |

Once every caller uses Entra ID, turn keys off completely: resource → **Resource Management** → **Keys and Endpoint** → disable local authentication.

---

## 11. Lab 7: RAG with Azure AI Search

[⬆ Back to Lab Index](#lab-index)

RAG grounds answers in your own documents without retraining the model.

```
INGESTION (once, then on a schedule)
  PDFs in Blob Storage ──> chunk ──> embed (text-embedding-3-small) ──> Azure AI Search index

QUERY (every question)
  Question ──> Azure AI Search (hybrid: keyword + vector, then semantic rerank)
                       │
                       └─> top chunks ──> gpt-5.4-mini ──> grounded answer with sources
```

The **Import data** wizard in Azure AI Search builds the whole ingestion side for you. This is called *integrated vectorization*.

**Cost warning:** this lab needs Azure AI Search on the **Basic** tier or higher (required for managed identity), which is billed per hour whether you use it or not. Delete it when you finish (Lab 10).

### Step 1: Storage account and sample documents

1. **Azure portal** → **Create a resource** → **Storage account** → **Create**.
2. Resource group `rg-genai-lab`, a unique name, region `East US 2`, performance **Standard**. **Review + create** → **Create**.
3. Open the storage account → **Data storage** → **Containers** → **+ Container** → name `docs` → **Create**.
4. Open `docs` → **Upload** → add a few PDFs. Microsoft's sample set: [health-plan PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan).

### Step 2: Azure AI Search service

1. **Azure portal** → **Create a resource** → **Azure AI Search** → **Create**.
2. Resource group `rg-genai-lab`, a unique service name, region `East US 2`, **Pricing tier: Basic**. **Review + create** → **Create**.
3. Open the search service → **Settings** → **Keys** → set API access control to **Role-based access control** (or **Both**).
4. **Settings** → **Identity** → **System assigned** → **On** → **Save**.

### Step 3: Role assignments

All of these use **Access control (IAM)** → **+ Add** → **Add role assignment**, exactly as in Lab 6.

| On this resource | Assign this role | To |
| :--- | :--- | :--- |
| Azure AI Search service | **Search Service Contributor** | You |
| Azure AI Search service | **Search Index Data Contributor** | You |
| Azure AI Search service | **Search Index Data Reader** | You |
| Storage account | **Storage Blob Data Reader** | The search service's managed identity |
| Foundry resource | **Foundry Project Manager** | The search service's managed identity |

For the last two, choose **Managed identity** on the **Members** tab and pick your search service.

### Step 4: Run the Import data wizard

1. Open the search service → **Overview** → **Import data**.
2. Data source: **Azure Blob Storage**. Scenario: **RAG**.
3. **Connect to your data:** pick your subscription, storage account and the `docs` container. Tick **Authenticate using managed identity** and keep **System-assigned**. **Next**.
4. **Vectorize your text:** Kind **Microsoft Foundry** → your subscription → project `genai-lab-project` → model deployment `text-embedding-3-small`. Authentication type **System assigned identity**. Tick the billing acknowledgement. **Next**.
5. **Vectorize and enrich your images:** skip. **Next**.
6. **Advanced settings:** enable **semantic ranker**, set the schedule to **Once**. **Next**.
7. **Review and create:** set the object name prefix to `rag-lab` → **Create**.

The wizard creates a data source, an index, a skillset and an indexer. It chunks text into pages of 2,000 characters with 500 characters of overlap. Index fields include `chunk` (the text), `title` (the file name) and `text_vector` (the embedding).

### Step 5: Test the index in the portal

1. Search service → **Search management** → **Indexes** → open your index (check the exact name here; you need it for the code).
2. In **Search explorer**, type a question about your documents, such as `Which plan has the lowest deductible?`, and select **Search**.
3. To read results easily, use **Query options** → **Hide vector values in search results**.

### Step 6: Ask questions from Python

```bash
pip install azure-search-documents azure-identity
```

Add to `.env`:

```env
SEARCH_ENDPOINT="https://<your-search-service>.search.windows.net"
SEARCH_INDEX="<index name from Step 5>"
```

`rag_app.py` (keyless for both services, so run `az login` first and complete Lab 6):

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

load_dotenv()
credential = DefaultAzureCredential()

search = SearchClient(
    endpoint=os.environ["SEARCH_ENDPOINT"],
    index_name=os.environ["SEARCH_INDEX"],
    credential=credential,
)
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
```

### RAG quality checklist

* **Chunking:** chunks too large dilute relevance, too small lose context. Overlap keeps sentences that span a boundary.
* **Hybrid search:** keyword plus vector finds both exact terms (product codes, names) and meaning.
* **Semantic ranker:** reranks the top results and usually improves answer quality noticeably.
* **Grounding instruction:** always tell the model to answer only from sources and to admit when it cannot.
* **Citations:** return the source file name so a user can verify the answer.
* **Access control:** filter search results by the user's permissions so RAG never leaks a document the user could not open.

For agents, **Foundry IQ** in the Foundry portal is the managed knowledge layer built on Azure AI Search. It turns your content into reusable, permission-aware knowledge bases.

---

## 12. Lab 8: Network Isolation with Private Endpoints

[⬆ Back to Lab Index](#lab-index)

By default the endpoint is reachable from the internet (protected by key or Entra ID). In production you normally remove the public path so that only your virtual network can reach the model.

```
+----------------------+    private IP inside your VNet    +-------------------------+
|  App Service / AKS   | ================================> |  Foundry resource       |
|  (managed identity)  |    via Private Endpoint           |  Public access: Disabled|
+----------------------+                                   +-------------------------+
```

### Option 1: Allow only chosen networks or IPs

1. **Azure portal** → Foundry resource → **Resource Management** → **Networking**.
2. Select **Selected networks**.
3. Add your virtual network and subnet, or add your public IP under **Firewall** → **Address range**.
4. **Save**.

### Option 2: Private endpoint only

1. Same **Networking** page → select **Disabled** → **Save**.
2. Open the **Private endpoint connections** tab → **+ Private endpoint**.
3. **Basics:** resource group `rg-genai-lab`, a name, the same region as your VNet.
4. **Resource:** target sub-resource **account**.
5. **Virtual Network:** choose the VNet and subnet your app can reach.
6. **DNS:** keep **Integrate with private DNS zone** set to **Yes**. Azure creates the zones `privatelink.cognitiveservices.azure.com`, `privatelink.openai.azure.com` and `privatelink.services.ai.azure.com`.
7. **Review + create** → **Create**.

After this, calls from your laptop fail and calls from inside the VNet succeed, with no code change, because the same hostname now resolves to a private IP.

Practice notes: do this lab last. With public access disabled you can no longer call the model from your own machine, and the Import data wizard in Lab 7 needs public access while it runs. Set it back to **All networks** to continue other labs.

---

## 13. Lab 9: Guardrails and Content Safety

[⬆ Back to Lab Index](#lab-index)

Every deployment has a guardrail that checks the prompt going in and the answer coming out. A new deployment gets the Microsoft default guardrail (**Default.V2**), which you cannot edit.

### What the default guardrail does

| Control | Checks | Default |
| :--- | :--- | :--- |
| **Hate, Sexual, Violence, Self-harm** | Prompt and completion, scored **safe / low / medium / high** | Blocks **medium** and **high** |
| **Prompt Shields: user prompt attacks** | Jailbreak attempts in the user's message | On |
| **Prompt Shields: indirect attacks** | Instructions hidden inside documents you pass in (important for RAG) | Off |
| **Protected material: text and code** | Known copyrighted text and public code in the output | Check the default list in the portal |

Optional controls you can add: **PII** detection and redaction, **groundedness** detection, and custom **blocklists**.

### What your app sees when something is blocked

* **Prompt blocked:** the call fails with HTTP `400` and error code `content_filter`. Catch it and show a friendly message.
* **Answer blocked:** the response comes back marked as filtered (in Chat Completions, `finish_reason` is `content_filter`). Do not show a half answer.

### Create and assign your own guardrail

Needs the **Foundry Account Owner** role.

1. **Foundry portal** → your project → **Build** → **Guardrails** in the left navigation.
2. Select **Create Guardrail**. Step 1 is **Add Controls**.
3. Pick a **risk** from the dropdown (for example indirect attacks, or PII).
4. Choose the **intervention points** (user input, output) and one **action**, then **Add control**.
5. To change a built-in control such as Violence, select the same risk again, change it, **Add control**, then **Confirm** the override.
6. **Next** → **Add models** → tick `gpt-5.4-mini` → **Save**.
7. **Next** → review, give it a name → **Create**.

### Test it

1. **Build** → **Guardrails** → select the row of your guardrail.
2. In the side panel select **Try in Playground**.
3. Send a prompt that should trip a control. When a blocking control fires, the chat shows which risk was detected and at which intervention point.

Each intervention point adds roughly 50 to 100 ms of latency, so add only the controls you need.

---

## 14. Lab 10: Cost Control and Clean-Up

[⬆ Back to Lab Index](#lab-index)

### What you pay for

* **Tokens in and tokens out,** priced per model. Output costs more than input.
* **Reasoning tokens** count as output. A high reasoning effort can cost far more than the visible answer suggests.
* **Azure AI Search** and **private endpoints** bill per hour while they exist.

### Ways to spend less

| Technique | How |
| :--- | :--- |
| **Right-size the model** | Use a mini or nano model by default; send only hard requests to a larger one, or let `model-router` choose |
| **Lower reasoning effort** | `low` or `minimal` is enough for most extraction, classification and summarising |
| **Cap output** | Set `max_output_tokens` on every call |
| **Cap the rate** | Keep tokens-per-minute low on the deployment so a bug cannot run up a bill |
| **Batch** | Global Batch is 50% cheaper for work that can wait up to 24 hours |
| **Prompt caching** | Put the long fixed part of the prompt first; repeated prefixes are billed at a discount automatically |
| **Cache answers** | Store answers to repeated questions in your own cache (for example Redis) |
| **Provisioned throughput (PTU)** | Reserve capacity when traffic is high and steady |

### Set a budget alert (Azure portal)

1. Search the top bar for **Cost Management + Billing** → **Cost Management** → **Budgets**.
2. Select **+ Add**. Set the **Scope** to the resource group `rg-genai-lab`.
3. Give it a name, a **Monthly** reset period and an amount (for example 10).
4. **Next** → add an alert at **80%** of **Actual** cost with your email → **Create**.

A budget only sends alerts. It does not stop spending.

### Watch usage

Foundry resource → **Monitoring** → **Metrics** shows requests and tokens per deployment. **Cost Management** → **Cost analysis**, filtered to `rg-genai-lab`, shows the money.

### Clean up everything

1. **Azure portal** → **Resource groups** → `rg-genai-lab`.
2. Select **Delete resource group**, type the name to confirm, **Delete**.

A deleted Foundry resource is kept in a soft-deleted state and still reserves its name. To reuse the name right away, search the portal for **Foundry**, open **Manage deleted resources**, select it and **Purge**.

<details>
<summary>▶ Azure CLI: delete and purge</summary>

```bash
az group delete --name rg-genai-lab --yes --no-wait

# Prints false when deletion has finished
az group exists --name rg-genai-lab

# Release the resource name immediately
az cognitiveservices account purge \
    --name foundry-genai-lab-<yourname> \
    --resource-group rg-genai-lab \
    --location eastus2
```

</details>

---

## 15. Lab 11: Prompt Engineering

[⬆ Back to Lab Index](#lab-index)

The model only knows what the prompt tells it. A clear prompt is the cheapest way to get a better answer.

### Techniques

| Technique | What to do | Example |
| :--- | :--- | :--- |
| **Be specific** | State the task, the audience, the length and the format | `Summarise for a new engineer in 3 bullet points.` |
| **Give a role** | Put the persona and rules in `instructions` | `You are a support agent for an insurance company.` |
| **Use delimiters** | Wrap pasted text in tags so it is not confused with your instructions | `<review> ...text... </review>` |
| **Show examples (few-shot)** | Give two or three input and output pairs in the style you want | See the script below |
| **Fix the output format** | Name the exact labels or fields allowed | `Answer with one word: Positive, Negative or Neutral.` |
| **Give a way out** | Say what to do when the answer is unknown | `If the text does not say, reply "Not stated".` |
| **Ground it** | Supply the facts and tell the model to use only those | The RAG prompt in Lab 7 |

With reasoning models, do not add "think step by step". The model already reasons internally; raise or lower **reasoning effort** instead. Describe the goal and the constraints, and let the model plan.

### Try it in the playground

1. **Foundry portal** → **Build** → **Models** → select **gpt-5.4-mini**.
2. Send this vague prompt: `Tell me about this review: The laptop is fast but the battery dies in two hours.`
3. Now send the specific version: `Classify the sentiment of the review inside the tags as Positive, Negative or Mixed, then give one reason in under 15 words. <review>The laptop is fast but the battery dies in two hours.</review>`
4. Compare the two answers. The second is short, predictable and easy for code to use.
5. Move the fixed part (`Classify the sentiment...`) into the instructions box and send only the tagged review as the prompt. This is how an app is normally structured.

### `prompt_few_shot.py`

Uses the same `.env` as Lab 4.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

# Rules plus two worked examples. Change these to change the behaviour.
instructions = """Classify the support ticket inside <ticket> tags.
Reply with exactly one label: Billing, Technical or Account.

<ticket>I was charged twice this month.</ticket>
Billing

<ticket>The app crashes when I open settings.</ticket>
Technical"""

ticket = "I cannot reset my password."

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    instructions=instructions,
    input=f"<ticket>{ticket}</ticket>",
    reasoning={"effort": "low"},
)
print(response.output_text)   # expected: Account
```

---

## 16. Lab 12: Structured Outputs (JSON)

[⬆ Back to Lab Index](#lab-index)

A prompt can ask for JSON, but the model may still add extra words or miss a field. **Structured outputs** guarantee that the answer matches a JSON schema you supply, so your code can parse it safely.

### `structured_output.py`

```python
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

# The shape you want back. Change the properties to change the output.
schema = {
    "type": "object",
    "properties": {
        "customer_name": {"type": "string"},
        "product": {"type": "string"},
        "sentiment": {"type": "string", "enum": ["Positive", "Negative", "Mixed"]},
        "issues": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["customer_name", "product", "sentiment", "issues"],
    "additionalProperties": False,
}

email = "Hi, this is Priya. My new X200 laptop is fast, but the battery dies in two hours and the fan is loud."

response = client.responses.create(
    model=os.environ["CHAT_DEPLOYMENT"],
    instructions="Extract the details from the customer email.",
    input=email,
    text={"format": {"type": "json_schema", "name": "ticket", "schema": schema, "strict": True}},
)

data = json.loads(response.output_text)   # always valid JSON in this shape
print(data["customer_name"], "|", data["sentiment"])
for issue in data["issues"]:
    print("-", issue)
```

### Schema rules in strict mode

* Every property must be listed in `required`.
* Every object needs `"additionalProperties": False`.
* For an optional value, allow null: `"type": ["string", "null"]`.
* Use `enum` to restrict a field to fixed choices.

Typical uses: extracting fields from emails, invoices and forms, classification with fixed labels, and any step where the next consumer is code and not a person.

---

## 17. Lab 13: Function Calling

[⬆ Back to Lab Index](#lab-index)

A model cannot look up live data or take actions on its own. With **function calling** you describe your functions to the model. When it needs one, it replies with the function name and arguments. **Your code** runs the function and sends the result back, and the model writes the final answer.

```
1. You  ──> question + list of available functions ──> Model
2. Model ──> "call get_order_status(order_id='A123')" ──> You
3. You run the function in your own code
4. You  ──> function result ──> Model
5. Model ──> final answer in plain language ──> You
```

The model never runs anything itself. You stay in control of what gets executed.

### `function_calling.py`

```python
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
MODEL = os.environ["CHAT_DEPLOYMENT"]

# Your real function. Replace the body with a database or API call.
def get_order_status(order_id: str) -> dict:
    orders = {"A123": "Shipped, arriving Friday", "B456": "Processing"}
    return {"order_id": order_id, "status": orders.get(order_id, "Not found")}

# The description the model sees. It must match the function above.
tools = [{
    "type": "function",
    "name": "get_order_status",
    "description": "Look up the delivery status of a customer order.",
    "parameters": {
        "type": "object",
        "properties": {"order_id": {"type": "string", "description": "Order ID, for example A123"}},
        "required": ["order_id"],
        "additionalProperties": False,
    },
}]

# Steps 1 and 2: ask, and let the model decide whether to call the function
response = client.responses.create(model=MODEL, input="Where is my order A123?", tools=tools)

# Step 3: run every function the model asked for
results = []
for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        print(f"Model asked for: {item.name}({args})")
        results.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(get_order_status(**args)),
        })

# Steps 4 and 5: send the results back and get the final answer
final = client.responses.create(
    model=MODEL,
    previous_response_id=response.id,
    input=results,
    tools=tools,
)
print(final.output_text)
```

### Good practice

* Write a clear `description` for the function and for each parameter. The model chooses from these words alone.
* Validate the arguments before you act on them. Treat them like any user input.
* Ask the user to confirm before a function that changes something (refund, delete, send email).
* If the question does not need a function, the model answers directly and `results` stays empty. Handle that case in a real app.

Function calling is the building block for agents: an agent is a model that calls tools in a loop until the task is done.

---

## 18. Troubleshooting

[⬆ Back to Lab Index](#lab-index)

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| `404 DeploymentNotFound` | `model` is not your deployment name, or the base URL is missing `/openai/v1/` | Copy the deployment name from **Build** → **Models**; check the base URL |
| `401 Unauthorized` | Wrong key, or key from a different resource | Re-copy **KEY 1** from **Keys and Endpoint** |
| `401` / `403` with keyless auth | Role missing or not applied yet, or signed in to the wrong tenant | Assign **Cognitive Services OpenAI User**, wait a few minutes, run `az login` again |
| `429 Too Many Requests` | Tokens-per-minute limit reached | Retry with backoff, or raise the limit on the deployment |
| `400` with code `content_filter` | Prompt blocked by the guardrail | Rephrase, or adjust the guardrail (Lab 9) |
| `400` unsupported parameter | Parameter the model does not accept, such as `temperature` or `max_tokens` | Remove it; use `max_output_tokens`, reasoning effort and verbosity |
| Empty or cut-off answer | `max_output_tokens` used up by reasoning | Raise the cap or lower reasoning effort |
| `410 Gone` | The model version was retired | Deploy the replacement model and update the deployment name |
| `DeploymentModelNotSupported` | Model, version or SKU not offered in your region | Pick another region or deployment type (Lab 2 CLI block lists what is offered) |
| Quota error when deploying | No quota left for that model in the region | Lower the tokens-per-minute value, free quota from another deployment, or request more |
| `CustomDomainInUse` | Resource name taken, often by your own soft-deleted resource | Choose another name or purge the old one (Lab 10) |
| Import data wizard fails | A resource has public access disabled, or a role is missing | Enable public access during the wizard; recheck the role table in Lab 7 |

---

## Reference Links

[⬆ Back to Lab Index](#lab-index)

* [Quickstart: set up Microsoft Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources)
* [Create a Foundry resource (Azure portal, CLI, PowerShell)](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource)
* [Deploy Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models)
* [Foundry Models sold by Azure (model list)](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure)
* [Model retirement schedule](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule) and [lifecycle policy](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements)
* [Deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)
* [Azure OpenAI v1 API](https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle)
* [Responses API](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses)
* [Reasoning models](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning)
* [Vector search quickstart: Import data wizard](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal-import-vectors)
* [Configure guardrails and controls](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails)

---

*Notes based on the Azure OpenAI crash course by Krish Naik, updated to the current Microsoft Foundry experience.*
