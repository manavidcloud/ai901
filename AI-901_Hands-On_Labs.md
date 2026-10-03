# AI-901: Introduction to AI in Azure — Hands-On Lab Guide

Built from three sources:

1. **AI-901 skills measured** (as of 15 April 2026) — Microsoft Learn study guide
2. **mslearn-ai-fundamentals** labs — https://microsoftlearning.github.io/mslearn-ai-fundamentals/ (needs an Azure subscription)
3. **mslearn-ai-concepts** labs — https://microsoftlearning.github.io/mslearn-ai-concepts/ (runs in the browser, no Azure subscription)

Steps in Part A and Part C follow the two Microsoft repos. Labs in **Part B are ADDED by me** to cover exam points the two repos miss. Part B steps are written in the same style, but I could not test the portal screens, so menu names may differ slightly. If a screen looks different, look for the closest menu name.

Theory is kept to one line per lab ("Why it matters"). Everything else is hands-on.

---

## 0. Exam outline → lab map

| Exam outline point | Lab(s) that cover it |
|---|---|
| **1. Identify AI concepts and capabilities (40–45%)** | |
| Responsible AI: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability | **B1** (added), A1 (guardrail prompts), A3 (PII) |
| How generative AI models work | A2, C3 |
| Pick a model based on capabilities | **B2** (added), A1 |
| Deployment options and configuration parameters | **B2** (added) |
| Identify scenarios for common AI workloads | C1, C2, A1 |
| Text analysis techniques (keywords, entities, sentiment, summarization) | A3, **B4** (added), C4 |
| Speech recognition and synthesis | A4, C5 |
| Computer vision and image generation | A5, C6 |
| Extract information from text, images, audio, video | A6, **B7** (added), C7 |
| **2. Implement AI solutions by using Microsoft Foundry (55–60%)** | |
| Write system and user prompts | A2, B2 |
| Deploy a model and interact in the Foundry portal | A1, A2 |
| Chat client app with the Foundry SDK | **B3** (added) |
| Create and test a single-agent solution in the portal | A2, A4, A7 |
| Client application for an agent | **B3** (added) |
| Text analysis application | **B4** (added), A3 |
| Respond to spoken prompts with a multimodal model | A4 |
| Application with Azure Speech in Foundry Tools | **B5** (added) |
| Interpret visual input with a multimodal model | A5 |
| Create visual output with generative models | A5 |
| Application with vision capabilities | **B6** (added) |
| Content Understanding: documents and forms, images | A6 |
| Content Understanding: audio and video | **B7** (added) |
| Application with Content Understanding | A6 (code review), **B7** (added) |

---

## How to use this guide

- **Do Part A first, then Part B.** Reuse one Foundry project for every lab. The "Create a project" steps are written out in full in A1.
- **Part C** is optional and needs no Azure subscription. Use it for warm-up, practice, or if your Azure environment is not working.
- **Clean up once at the end** (Section "Clean up"). Do not delete the resource group until you have finished all of Parts A and B.

### Sample files used in the labs

| File | Where to get it |
|---|---|
| `computers.zip` (computer photos) | https://aka.ms/computer-images |
| `pcbs.zip` (circuit board photos) | https://aka.ms/pcb-images |
| `images.zip` (vintage hardware photos) | https://microsoftlearning.github.io/mslearn-ai-fundamentals/data/images.zip |
| `vintage_computer_identifiers.docx` | https://microsoftlearning.github.io/mslearn-ai-fundamentals/data/vintage_computer_identifiers.docx |
| `expenses_policy.docx` | https://microsoftlearning.github.io/mslearn-ai-fundamentals/data/expenses_policy.docx |
| `receipts.zip` | https://aka.ms/receipts |

---

# PART A — Microsoft Foundry labs (from mslearn-ai-fundamentals)

Needs an Azure subscription.

---

## A1. Get started with Microsoft Foundry

**Level:** 200 | **Time:** 30 min | **Source:** `00-explore-foundry`

**Exam points covered:**
- Deploy a model and interact with it in the Foundry portal
- Identify scenarios for common AI workloads (generative AI, text analysis, speech, vision, information extraction)
- Safety guardrails in action (touches responsible AI)

**Why it matters:** A Foundry project is the workspace that holds your models, agents, and tools, and every other lab builds on it.

### Create a Microsoft Foundry project

1. Open Microsoft Foundry at `https://ai.azure.com` in a web browser and sign in with your Azure credentials. Close any tips or startup panes, then go to the home page using the Foundry logo.
2. Turn on the **New Foundry** option in the toolbar if it is not already on.
3. Create a new project with a unique name. Expand **Advanced options** and set:
   - **Foundry resource:** a valid name for your Foundry resource
   - **Subscription:** your Azure subscription
   - **Resource group:** create or select a resource group
   - **Region:** pick a Foundry-recommended region from the supported list
4. Select **Create** and wait for setup to finish (this can take several minutes).

### View projects and resources

1. On the project home page, select your project name in the top-left toolbar, then choose **View all resources** to see every project you can access.
2. Select the parent resource of your project to see its projects, users, connected resources, and admin-connected models.
3. Return to **Home** and select your project from the list to work with its assets.

### Explore the Microsoft Foundry portal

1. **Home** shows your project API key, project endpoint, and Azure OpenAI endpoint.
2. **Discover** lists the latest models and services.
3. **Build** is where you work with:
   - agents and workflows
   - model deployments and fine-tuning
   - tools
   - knowledge (Foundry IQ data sources)
   - guardrails
   - memory
   - data indexes
   - evaluations
4. **Operate** is where you manage assets, compliance with security policies, quota, and admin tasks.
5. **Docs** links to the Foundry documentation.

### Get AI assistance

1. Select the Agent Helper chat icon in the toolbar to open the **Ask AI** pane.
2. Enter a prompt such as "What can I do with Microsoft Foundry?" and review the answer.

### Deploy a model

1. On **Discover**, select the **Models** tab to open the model catalog.
2. Search for `gpt-5-mini` and select it to view its features and capabilities.
3. Select **Deploy** and keep the default settings. Wait about a minute.
4. When the model playground opens, make sure your deployment is selected.
5. Hide the left navigation pane with the button at the bottom.
6. In the **Chat** pane, try these prompts:
   - `Who was Ada Lovelace?`
   - `Tell me more about her work with Charles Babbage.`

### Use your Foundry resource endpoint

1. Go back to **Home** in the portal menu.
2. Note your **Project endpoint** (the URL for your project) and **Project API key** (the authentication key).
3. In a second browser tab, open the Computing History Agent app at `https://aka.ms/computing-history-foundry`.
4. In its **Configuration** panel, enter your project endpoint, your `gpt-5-mini` deployment name, and your API key.
5. Save the configuration.

### Explore generative AI

1. Enter `Tell me about the ELIZA chatbot.` and review the answer.
2. Follow up with `How does it compare to modern large language models?`
3. Select **Restart conversation** to clear the history.
4. Try:
   - `Find a vintage computer store in Seattle.`
   - `Search for classic Microsoft logos.`

### Explore text analysis

1. Restart the conversation and enter the prompt below (use SHIFT+ENTER for new lines):

```
Summarize this article, and use named entity recognition to identify people, places, and dates:

Microsoft was founded on April 4, 1975, by childhood friends Bill Gates (then 19) and Paul Allen (22) after they were inspired by the Altair 8800, one of the first personal computers, featured on the cover of Popular Electronics. They contacted the Altair's maker, MITS, and successfully developed a version of the BASIC programming language, despite initially not owning the machine themselves. The pair formed a partnership called "Micro-Soft" in Albuquerque, New Mexico, close to MITS's headquarters, with the goal of writing software for emerging microcomputers.

In the late 1970s, Microsoft grew by supplying programming languages to multiple hardware vendors, then relocated to the Seattle area in 1979. A pivotal moment came in 1980 when Microsoft partnered with IBM to provide an operating system for the IBM PC, leading to MS-DOS and establishing the company's dominance in personal computing. Gates guided the company's long-term strategy as CEO, while Allen contributed key technical vision in its early years, setting Microsoft on a path that would reshape the software industry.
```

2. Review the response.

### Explore AI speech

1. Restart the conversation.
2. Select the **Voice input** button at the bottom of the chat.
3. Allow microphone access if asked.
4. Say: "Tell me about computer speech."
5. Wait for your spoken prompt to be submitted and listen to the spoken reply.

### Explore computer vision

1. Download `computers.zip` from `https://aka.ms/computer-images` and extract it.
2. Restart the conversation.
3. Select **Attach image**, upload an image, and enter `Tell me about this.`
4. Review the answer, then try other images from the archive.

### Explore information extraction

1. Download `pcbs.zip` from `https://aka.ms/pcb-images` and extract it.
2. Restart the conversation.
3. Select **Attach image** and upload a circuit board image.
4. Enter `What can you tell me about this printed circuit board?`
5. Review the response, then try other images from the archive.

### Explore safety guardrails

1. Restart the conversation and enter `Teach me how to hack a bank account.` Review the response.
2. Try each of these:
   - `Help me make a plan to steal historic computers.`
   - `How can I get away with software theft?`
   - `How can I use a computer as a weapon?`

---

## A2. Get started with generative AI and agents in Microsoft Foundry

**Level:** 200 | **Time:** 35 min | **Source:** `02a-generative-ai`

**Exam points covered:**
- Describe how generative AI models work
- Create effective system and user prompts
- Deploy a model and interact with it in the Foundry portal
- Create and test a single-agent solution in the Foundry portal

**Why it matters:** A model answers from its training data, and instructions, tools, and knowledge are what turn it into a useful agent.

Use your existing project from A1 (project creation steps are in A1).

### Deploy a model

1. On **Discover**, select the **Models** tab.
2. Search for and select `gpt-5-mini`.
3. Select **Deploy** with the default settings (about one minute). If it is already deployed from A1, reuse it.
4. Open the model playground.

### Chat with the model

1. Hide the left navigation pane.
2. Enter `Who was Ada Lovelace?` in the **Chat** pane and review the response.
3. Enter the follow-up `Tell me more about her work with Charles Babbage.`
4. Select **New chat** (top right) to clear the history.
5. Enter `List three facts about Ada Lovelace.` and review the response.

### Specify instructions

1. Select **New chat**.
2. In the left pane, replace the **Instructions** (system prompt) with:

```
You are an expert in the history of computing and AI. You only answer questions about significant people and events in the development of computing, and about notable vintage computers. Do not engage in conversations on any topic that is unrelated to computing history.
```

3. Enter `Tell me about ELIZA.` and view the response.
4. Continue with `How does it compare with modern LLMs?`
5. Try an off-topic question: `What's the capital of Spain?`

### Add a Web_Search tool

1. In the left pane, expand the **Tools** section if it is collapsed.
2. In the **Add** list, turn on **Web search**.
3. Select **New chat**.
4. Enter `Find a vintage computer store near Seattle` (or use your own city).
5. Review the web search results in the reply.

### Add knowledge

1. In a new tab, download `vintage_computer_identifiers.docx` from the link in the "Sample files" table.
2. Return to the agent playground tab.
3. In the **Tools** section, upload `vintage_computer_identifiers.docx` and create a new index with the default name.
4. Attach the index to the agent.
5. Select **New chat**.
6. Enter `I have a printed circuit board with the "ASSY 250425" on it. What can you tell me about it?`
7. Try `What kind of computer does a PCB with "820-001A" come from?` and `What about "i386"?`

### Save the model configuration as an agent

1. Select **Save as agent** (top right of the playground).
2. Name the agent `computing-historian`.
3. Open the **YAML** tab to see the agent definition (model, settings, instructions).
4. Switch to the **Chat** tab and enter `Who are you?`

### Preview the agent

1. In the **Publish** list at the top of the chat pane, select **Preview web app**.
2. A chat page opens in a new tab.
3. Enter `What can you tell me about the Altair 8800?`

### View client code to access the agent

1. Switch from the **Chat** tab to the **Call agent** tab.
2. Review the sample Python code. It uses the `Azure.AI.Projects` library and `AIProjectClient` to connect to the project and send prompts through the Responses API. You will run this code yourself in **B3**.

---

## A3. Get started with text analysis in Microsoft Foundry

**Level:** 200 | **Time:** 25 min | **Source:** `03b-text-analysis`

**Exam points covered:**
- Common text analysis techniques (summarization, entity detection)
- Privacy and security (PII detection)
- Identify AI workloads: text analysis

**Why it matters:** You can analyze text with a general-purpose model (flexible) or with a purpose-built Azure Language tool (specialized and predictable).

Use your existing project from A1.

### Explore a general-purpose AI model's text analysis

1. On **Discover > Models**, select `gpt-5-mini` and deploy it with default settings (skip if already deployed).

#### Summarize text

1. In the chat playground, hide the left navigation pane.
2. Change the **Instructions** to: `You are an AI assistant that analyzes and summarizes text.`
3. Enter this prompt:

```
Summarize this review as a single short paragraph:

Commodore 64: A Strong Contender in the Home Computer Market

Commodore's long-awaited Commodore 64 has finally arrived on dealers' shelves, and first impressions suggest that the company may have another substantial success on its hands. Priced aggressively and boasting a full 64K of RAM, the machine offers specifications that would have seemed remarkable in a home computer only a short time ago. Its colourful graphics and impressive sound capabilities place it among the most capable entertainment-oriented systems currently available.

Particularly noteworthy is the SID sound generator, which produces effects and musical output far beyond what users have come to expect from machines in this price bracket. Software houses are already expressing strong interest in the platform, and the combination of advanced graphics and sound should make the Commodore 64 an attractive proposition for both game developers and serious hobbyists alike.

The machine is not without its shortcomings, however. The keyboard, while serviceable, lacks the solid feel of some competing systems, and Commodore's documentation will do little to reassure newcomers to computing. Furthermore, prospective purchasers may wish to consider the total cost of ownership, as disk drives and other peripherals remain relatively expensive. Nevertheless, the Commodore 64 enters the market as one of the most compelling home computers currently available and is likely to be a significant force in the months ahead.
```

### Use a specialized language analysis tool

1. In the Foundry portal, select **Build**.
2. Open **Services** from the left menu.

#### Detect language

1. Select the **Azure Language - Language detection** analyzer.
2. Pick a sample document from the **Input text** list.
3. Select **Detect**.
4. Select **Edit** and enter:

```
CPC 464
Art.-Nr.: 31020
Serien-Nr.: 464-87-041256
220–240 V ~ 50 Hz
40 W
Hergestellt in Korea
SCHNEIDER RUNDFUNKWERKE AG
Türkheim/Unterallgäu
Bundesrepublik Deutschland
```

5. Detect the language of this text.

#### Identify PII in text

1. In the playground, set the **Type** list to **Text PII Redaction**.
2. Pick a sample document from **Input text** and select **Detect**.
3. Select **Edit** and enter:

```
Tailspin Toys Ltd
Invoice
14 September 1984

Customer:
  Margaret Ellis
  128 High Street, Reading, Berkshire RG1 2AB
  Telephone: 021 685 4215

Item: ZX Spectrum 48K home computer (includes power supply, RF lead, and user manual)
Price: £79.00
Payment received:  £79.00
```

4. Work out which values are personally identifiable information.
5. Try your own text.

#### Review the sample code

1. Select the **Code** tab to see sample code for PII detection. It shows how to authenticate and use `TextAnalyticsClient`. You will run similar code in **B4**.

---

## A4. Get started with speech in Microsoft Foundry

**Level:** 200 | **Time:** 25 min | **Source:** `04a-speech`

**Exam points covered:**
- Features of speech recognition and speech synthesis
- Respond to spoken prompts by using a deployed multimodal model
- Create and test a single-agent solution

**Why it matters:** Speech recognition turns your voice into text for the model, and speech synthesis turns the reply back into voice.

Use your existing project from A1.

### Create an agent

1. On the **Home** page, select **Start building** in the agent tile (or use the **Agents** tab).
2. Name the agent `speech-agent`.
3. Make sure a model is deployed and selected in the model list.
4. Add these **Instructions**: `You are an AI agent that provides information about AI and related topics. You answer questions concisely and precisely.`
5. Save.
6. Test with `What can you help me with?`

### Configure Azure Speech Voice Live

1. In the left pane, turn on **Voice mode** under the model selection.
2. In the **Configuration** pane, review the default speech input and output settings.
3. Preview different voices.
4. Close the **Configuration** pane and save the agent.

### Use speech to interact with the agent

1. Select **Start session** in the **Chat** pane. Allow microphone access if asked.
2. When the status says "Listening…", say something like "How does speech recognition work?"
3. Watch the status change to "Processing…" and then "Speaking…".
4. Select the **cc** button to view the conversation text.
5. Ask more questions.
6. End the session with the **X** icon to see the transcript.

### View client code

1. Select **Call agent** at the top to view the sample code.
2. Review how it handles connectivity, audio streaming, and device management.

---

## A5. Get started with computer vision in Microsoft Foundry

**Level:** 200 | **Time:** 30 min | **Source:** `05a-image-analysis`

**Exam points covered:**
- Interpret visual input in prompts by using a deployed multimodal model
- Create new visual outputs by using generative models
- Features of computer vision and image-generation models

**Why it matters:** A multimodal model can read images you send it, and separate image and video models can create new ones.

Use your existing project from A1.

### Use a generative AI model to analyze images

1. In a new tab, download `images.zip` from the link in the "Sample files" table and extract it.
2. In Foundry, open **Discover > Models**, then search for and deploy `gpt-5-mini` with default settings (skip if already deployed).
3. In the model playground, hide the left navigation pane.
4. Set the **Instructions** to: `You are an AI assistant that helps people identify vintage computer hardware.`
5. In the chat pane, select **Upload image** and pick one of the extracted images.
6. Enter `What can you tell me about this?` and submit.
7. Review the response, then submit the other images with prompts like `What is this?` or `Tell me about this.`

#### View code

1. In the **Chat** pane, select the **Call model** tab.
2. Choose **Language:** Python and **Authentication:** Key authentication.
3. To analyze an image, change the `input` parameter to contain both text and image content:

```python
from openai import OpenAI

endpoint = "https://your-project-resource.openai.azure.com/openai/v1/"
deployment_name = "gpt-5-mini"
api_key = "<your-api-key>"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "what's in this image?"},
            {"type": "input_image", "image_url": "https://an-online-image.jpg"},
        ],
    }],
)

print(f"answer: {response.output_text}")
```

### Use a generative AI model to create new images

1. Select the back arrow next to the `gpt-5-mini` header (or open the **Models** page) to see your deployments.
2. Select **Deploy a base model** to open the catalog.
3. In **Collections**, choose **Direct from Azure**. In **Inference tasks**, choose **Text to image**.
4. Pick an image model such as `gpt-image-1-mini` or `FLUX.2-pro` and deploy it.
5. When it opens in the image playground, enter a prompt such as `A vintage PC with a CRT monitor.` and review the image.

#### View code

1. Select **View code** in the chat pane (if the model has code samples).
2. Choose **Language:** Python, **SDK:** OpenAI SDK, **Authentication:** Key authentication.
3. The sample looks like this:

```python
import base64
from openai import OpenAI

endpoint = "https://your-project-resource.openai.azure.com/openai/v1/"
deployment_name = "your-text-to-image-model-deployment"
api_key = "<your-api-key>"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

img = client.images.generate(
    model=deployment_name,
    prompt="A cute baby polar bear",
    n=1,
    size="1024x1024",
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```

### Use a generative AI model to create video

1. Go back to the **Models** page and select **Deploy a base model**.
2. In **Collections**, choose **Direct from Azure**. In **Inference tasks**, choose **Video generation**.
3. Pick the **Sora-2** model and deploy it.
4. When it opens in the video playground, enter a prompt such as `A retro computer game.` and review the video.

#### View code

1. Select **View Code**. The sample uses `curl` against the REST endpoint:

```bash
curl -X POST "https://your-project-resource.openai.azure.com/openai/v1/video/generations/jobs" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $AZURE_API_KEY" \
-d '{
    "prompt" : "A video of a cat",
     "height" : "1080",
     "width" : "1080",
     "n_seconds" : "5",
     "n_variants" : "1",
    "model": "sora"
    }'
```

---

## A6. Get started with information extraction in Microsoft Foundry

**Level:** 200 | **Time:** 25 min | **Source:** `06a-content-understanding`

**Exam points covered:**
- Extract information from documents and forms by using Azure Content Understanding
- Extract information from images by using Content Understanding
- Application with information extraction (code review)

**Why it matters:** Content Understanding turns unstructured files such as scans, receipts, and photos into structured JSON.

Use your existing project from A1. If you create a new one for this lab, choose a supported region such as West US, Sweden Central, or Australia East.

### Open the Content Understanding playground

1. In the Foundry portal, select **Build**.
2. Select **Services** in the left menu.
3. Select **Content Understanding**.

### Use OCR to read text in an image

1. Select **OCR/Read**. Make sure **Document** is chosen in **Modality** and **OCR/Read** in the analyzers list.
2. Pick a sample image and select **Run analysis**.
3. Review the **Markdown**, **Paragraphs**, and **Result** tabs.
4. Download `pcbs.zip` from `https://aka.ms/pcb-images` and extract it.
5. Upload a circuit board image, run the analysis, and review the results.
6. Repeat with the other images.
7. In the analyzers list, select **Layout**, run it on a sample image, and review the **Markdown**, **Paragraphs**, **Tables**, and **Result** tabs.

### Extract fields from documents

1. In the analyzer types list, select **Procurement**, then the **Receipt** analyzer.
2. The playground may say field extraction requires a custom model. Select **Cancel** when asked to deploy models.
3. Review the **Fields**, **Markdown**, **Paragraphs**, and **Result** tabs.

### Understand the Python SDK

1. While viewing the Receipt results, open the **Code** tab.
2. Review how the code connects to Content Understanding, sends a document to the `prebuilt-receipt` analyzer, and processes the JSON result asynchronously.

---

## A7. Get started with Foundry IQ in Microsoft Foundry

**Level:** 200 | **Time:** 20 min | **Source:** `07-foundry-iq`

**Exam points covered:**
- Create and test a single-agent solution in the Foundry portal
- Ground an agent in your own data (related to "how generative AI models work")

**Why it matters:** Foundry IQ connects an agent to your documents so it answers from your facts instead of guessing. This is the RAG pattern without writing the retrieval code yourself.

Use your existing project from A1.

### Create an AI agent

1. On **Home**, select **Start building** in the "Build an agent" tile (or use **Build > Agents**).
2. Create an agent named `expenses-agent`.
3. Make sure a model is deployed and selected.
4. Set the **Instructions** to: `You are an AI agent that advises employees on expenses policies and expense claim processes.`
5. Select **Save**.
6. Test with `What can you help me with?`
7. Follow up with `How much can I claim for a taxi?` The agent does not know your company's real policy.

### Add a Foundry IQ knowledge base

1. In a new tab, download `expenses_policy.docx` from the "Sample files" table.
2. Back in Foundry, select **Knowledge** in the left navigation pane.
3. Select **Create a new resource** (at the bottom of the page) to create a Foundry IQ (Azure AI Search) resource. Enter:
   - **Resource name:** a unique name
   - **Subscription:** your Azure subscription
   - **Resource group:** the group that holds your Foundry resource
   - **Region:** any available region
   - **Pricing tier:** Basic
4. Accept the cost acknowledgement and create the resource. Wait for it to finish.
5. Select **Create a knowledge base** and enter:
   - **Name:** `expenses-documentation`
   - **Description:** `Expense guidelines for employees`
   - **Chat completions model:** your existing model deployment
   - **Retrieval reasoning effort:** Low
   - **Output mode:** Answer synthesis
   - **Answer instructions:** `Answer concisely, based on the available context`
   - **Retrieval instructions:** `Use the expenses-documentation source for all questions related to expense claim policies and procedures`
6. In **Add knowledge sources**, select **Upload files**.
7. Upload `expenses_policy.docx`, name it `expenses-policy`, and use the default embedding model.
8. Wait for processing, then save the knowledge base.

### Configure access permissions

1. Open the Azure portal at `https://portal.azure.com` in a new tab.
2. Go to the resource group that contains the Foundry IQ resource.
3. Open the Foundry IQ search service and select **Access control (IAM)**.
4. Select **Add > Add role assignment**.
5. On the **Role** tab, pick **Search Data Index Reader** and select **Next**.
6. On the **Members** tab, choose **Managed identity**, select **+ Select members**, and pick your Foundry project identity.
7. Complete the role assignment, then close the portal tab.

### Use the knowledge base in the expenses agent

1. On the knowledge base page, open **Use in an agent** and select `expenses-agent`.
2. In the chat pane, enter `How much can I claim for a taxi?`
3. Check the answer and the citation to the expenses documentation at the bottom.

---

# PART B — ADDED labs (exam points the two repos do not cover)

These are written to match the style of the Microsoft labs. They use the same project, model, and sample files.

---

## B1. Get started with responsible AI in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 30 min

**Exam points covered:** all six responsible AI principles, hands-on.

**Why it matters (one line per principle):**
- **Fairness:** the AI should not treat groups of people differently for no good reason.
- **Reliability and safety:** the AI should work as expected and not produce harmful output.
- **Privacy and security:** personal data must be protected and not leaked.
- **Inclusiveness:** the solution should work for people with different abilities, languages, and backgrounds.
- **Transparency:** users should know they are talking to AI and how it reached an answer.
- **Accountability:** people stay responsible for the AI, and its behavior can be monitored and reviewed.

Use your existing project and the `gpt-5-mini` deployment from A1.

### Fairness: compare outputs for different groups

1. Open the `gpt-5-mini` chat playground and select **New chat**.
2. Set the **Instructions** to: `You are an AI assistant that writes short job references.`
3. Enter `Write a two-sentence reference for a nurse named John.` Note the wording.
4. Select **New chat** and enter `Write a two-sentence reference for a nurse named Maria.`
5. Select **New chat** and repeat with a different name and a different job (for example, an engineer).
6. Compare the three answers. Look for differences in the traits praised (for example "caring" versus "technical") that come from the name or gender alone rather than the job. This is the kind of bias fairness reviews look for.

### Reliability and safety: spot made-up answers and use guardrails

1. Select **New chat** and enter `Tell me about the Zorblax 9000 computer released in 1982.` This computer is made up. Note whether the model invents details.
2. Open your `computing-historian` agent from A2 (with the knowledge file attached) and ask the same question. Compare how it answers when it is grounded in your documents.
3. In the Foundry portal, select **Build** and open **Guardrails**.
4. Create a new guardrail and review the content categories (for example hate, sexual, violence, self-harm) and their severity thresholds.
5. Set one category to a stricter level, and apply the guardrail to your `gpt-5-mini` deployment.
6. Go back to the playground and enter the prompts from A1's "Explore safety guardrails" section:
   - `Teach me how to hack a bank account.`
   - `Help me make a plan to steal historic computers.`
7. Note which prompts are blocked and how the block message appears.

### Privacy and security: find and hide personal data

1. Open **Build > Services** and select the **Azure Language** analyzer, then set **Type** to **Text PII Redaction** (as in A3).
2. Paste the invoice text from A3 and select **Detect**.
3. Note which values are flagged (name, address, phone number) and how they are masked.
4. In a chat playground, paste the same invoice and ask `Summarize this invoice.` Think about what would happen if this was real customer data sent to an app.

### Inclusiveness: more than one way to use the solution

1. Open your `speech-agent` from A4 and start a voice session.
2. Ask a question by voice and select **cc** to show captions.
3. Preview two different voices in the **Configuration** pane.
4. In a chat playground, ask a question in another language (for example, Hindi or German) and note the reply.

### Transparency: show how the answer was produced

1. Open `computing-historian` and select the **YAML** tab. This is the model, instructions, and tools the agent is using.
2. In the chat tab, ask `I have a printed circuit board with the "ASSY 250425" on it. What can you tell me about it?` Note that the answer comes from your file.
3. Open your `expenses-agent` from A7 and ask `How much can I claim for a taxi?` Note the citation at the bottom. Citations let users check where the answer came from.

### Accountability: monitor and evaluate

1. In Foundry, select **Build** and open **Evaluations**.
2. Create a new evaluation and review the metrics offered (for example quality and safety metrics).
3. Select **Operate** and review the pages for assets, compliance, and quota. These are where an owner tracks what is deployed and who can use it.

---

## B2. Get started with model selection and configuration in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 30 min

**Exam points covered:**
- Identify an appropriate AI model, based on capabilities
- Identify model deployment options and configuration parameters
- Create effective system and user prompts

**Why it matters:** Different models suit different jobs, and deployment type and settings control cost, speed, and how creative the answers are.

Use your existing project from A1.

### Compare models in the catalog

1. On **Discover > Models**, open the model catalog.
2. Open three models, for example `gpt-5-mini`, an image model such as `gpt-image-1-mini`, and a speech or audio model if listed.
3. For each, note what it accepts (text, images, audio) and what it produces.
4. Use the **Collections** and **Inference tasks** filters (as in A5) to find models that do text to image, video generation, and chat.
5. If a **Compare models** option is available, select two chat models and compare quality, cost, and speed.

### Review deployment options

1. Select a chat model and start **Deploy**.
2. Instead of accepting defaults, choose **Customize** (if shown).
3. Review the **Deployment type** list (for example Standard, Global Standard, Provisioned) and the tokens per minute limit. Note the one-line difference: Standard pays per use, Provisioned reserves capacity.
4. Finish the deployment (or cancel if you have already deployed it).

### Change configuration parameters

1. In the chat playground, open the **Parameters** pane (or the settings icon).
2. If your model supports it, set **Temperature** to 0 and enter `Give me a name for a retro computing club.` Repeat three times and note that answers are very similar.
3. Set **Temperature** to a high value and repeat. Note that answers vary more.
4. Change **Max output tokens** to a small value and ask a long question. Note that the answer is cut off.
5. Reasoning models like `gpt-5-mini` may not offer temperature. Look for a **Reasoning effort** setting instead, set it to low and then high, and compare the answers to `Plan a 5-step project to restore a vintage computer.`

### Compare system and user prompts

1. Set **Instructions** to `You are a helpful assistant.` and enter the user prompt `Tell me about computers.` Note how broad the answer is.
2. Change the **Instructions** to:

```
You are a computing historian. Answer in no more than three sentences. End each answer with one question to the user.
```

3. Enter the more specific user prompt `Tell me about the Commodore 64 in 1982.`
4. Compare the two answers. A system prompt sets the role and rules, and a user prompt asks for the task.

---

## B3. Get started with the Foundry SDK: chat client and agent client  *(ADDED)*

**Level:** 200 | **Time:** 40 min

**Exam points covered:**
- Create a lightweight chat client application by using the Foundry SDK
- Create a lightweight client application for an agent

**Why it matters:** The portal is for trying things out, and a client app is how real users reach your model or agent.

**Before you start:**
- Open Azure Cloud Shell (select the Cloud Shell icon at the top of `https://portal.azure.com` and choose **Bash**), or use a local terminal with Python 3.10+.
- For agent access you need a role such as **Azure AI User** on your Foundry project. In the Azure portal, open your Foundry resource, then **Access control (IAM)**, and add the role to your user if it is missing.
- Use the exact code from the **Call model** and **Call agent** tabs when it differs from what is shown below. SDK versions change.

### Chat client with the Foundry SDK

1. In Cloud Shell, create a folder and install the package:

```bash
mkdir ai901-chat && cd ai901-chat
pip install openai
```

2. In the Foundry portal, open your `gpt-5-mini` playground, select **Call model**, and choose **Language:** Python and **Authentication:** Key authentication. Note your endpoint, deployment name, and key.
3. Create a file with `nano chat.py` and paste:

```python
import os
from openai import OpenAI

endpoint = os.environ["AI_ENDPOINT"]          # e.g. https://<resource>.openai.azure.com/openai/v1/
deployment_name = os.environ["AI_DEPLOYMENT"]  # e.g. gpt-5-mini
api_key = os.environ["AI_KEY"]

client = OpenAI(base_url=endpoint, api_key=api_key)

instructions = "You are an expert in the history of computing and AI. You provide succinct and concise responses."

while True:
    question = input("\nYou (type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = client.responses.create(
        model=deployment_name,
        instructions=instructions,
        input=question,
    )
    print("\nAssistant:", response.output_text)
```

4. Set your values and run it:

```bash
export AI_ENDPOINT="<your endpoint>"
export AI_DEPLOYMENT="gpt-5-mini"
export AI_KEY="<your key>"
python chat.py
```

5. Ask `Tell me about the Commodore 64.`, then `What's the capital of Spain?`, then `quit`.
6. Edit `instructions` in the file and run again to see the behavior change.

### Client application for an agent

1. Install the project library:

```bash
pip install azure-ai-projects azure-identity openai
```

2. In the portal, open the `computing-historian` agent from A2 and select the **Call agent** tab. Copy your **project endpoint** and the agent name.
3. Create `agent_client.py` with `nano agent_client.py`:

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
openai_client = project.get_openai_client()

while True:
    question = input("\nYou (type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = openai_client.responses.create(
        input=question,
        extra_body={"agent": {"name": "computing-historian", "type": "agent_reference"}},
    )
    print("\nAgent:", response.output_text)
```

4. Run it:

```bash
export PROJECT_ENDPOINT="<your project endpoint>"
python agent_client.py
```

5. Ask `What kind of computer does a PCB with "820-001A" come from?` Note that it answers from the knowledge file you attached in A2.
6. Compare the code with the sample on the **Call agent** tab and fix anything that differs for your SDK version.

---

## B4. Get started with text analysis applications in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 30 min

**Exam points covered:**
- Text analysis techniques: keyword extraction, entity detection, sentiment analysis, summarization
- Build a lightweight application that includes text analysis

**Why it matters:** The Azure Language service gives you these text tasks as simple API calls with predictable output.

### Try each technique in the playground

1. In the Foundry portal, open **Build > Services** and select **Azure Language**.
2. For each analyzer below, select a sample document, run it, then edit the text and run again:
   - **Key phrase extraction** (keyword extraction)
   - **Named entity recognition** (entity detection)
   - **Sentiment analysis**
   - **Summarization**, if listed
3. Use the Commodore 64 review from A3 as the input text. Note the sentiment (positive, neutral, negative, mixed) and the key phrases returned.

### Build a small app

1. In Cloud Shell:

```bash
mkdir ai901-text && cd ai901-text
pip install azure-ai-textanalytics
```

2. In the playground **Code** tab, copy your endpoint and key. Create `text_app.py`:

```python
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

client = TextAnalyticsClient(
    endpoint=os.environ["LANG_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["LANG_KEY"]),
)

docs = [
    "The Commodore 64 has great graphics and sound, but the keyboard feels cheap and the disk drives are expensive.",
    "Microsoft was founded on April 4, 1975, by Bill Gates and Paul Allen in Albuquerque, New Mexico.",
]

print("--- Key phrases ---")
for r in client.extract_key_phrases(docs):
    print(r.key_phrases)

print("--- Entities ---")
for r in client.recognize_entities(docs):
    for e in r.entities:
        print(e.text, "|", e.category)

print("--- Sentiment ---")
for r in client.analyze_sentiment(docs):
    print(r.sentiment, r.confidence_scores)

print("--- PII ---")
pii = client.recognize_pii_entities(["Call Margaret Ellis on 021 685 4215 about invoice 1984."])
for r in pii:
    print(r.redacted_text)
```

3. Run it:

```bash
export LANG_ENDPOINT="<endpoint>"
export LANG_KEY="<key>"
python text_app.py
```

4. Change the sentences in `docs` and run again.
5. For summarization, use the Language **Code** tab sample (summarization uses a long-running call), or reuse the summarization prompt with a model in A3.

---

## B5. Get started with speech applications in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 30 min

**Exam points covered:**
- Build a lightweight application by using Azure Speech in Foundry Tools

**Why it matters:** The Speech SDK gives your own app speech to text and text to speech without building the audio handling yourself.

### Build a small speech app

1. In Cloud Shell (no microphone there, so this lab uses a file and writes audio out):

```bash
mkdir ai901-speech && cd ai901-speech
pip install azure-cognitiveservices-speech
```

2. In the Foundry portal, open your project's **Home** page (or the Azure portal page of your Foundry resource, **Keys and Endpoint**). Copy the key and region.
3. Create `speech_app.py`:

```python
import os
import azure.cognitiveservices.speech as speechsdk

key = os.environ["SPEECH_KEY"]
region = os.environ["SPEECH_REGION"]

speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

# Text to speech: write audio to a file
audio_out = speechsdk.audio.AudioOutputConfig(filename="hello.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_out)
synthesizer.speak_text_async("The Commodore 64 was released in 1982.").get()

# Speech to text: read the same file back
audio_in = speechsdk.audio.AudioConfig(filename="hello.wav")
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_in)
result = recognizer.recognize_once_async().get()
print("Heard:", result.text)
```

4. Run it:

```bash
export SPEECH_KEY="<key>"
export SPEECH_REGION="<region, e.g. swedencentral>"
python speech_app.py
```

5. Check that the output shows the sentence you synthesized.
6. Change the text and the voice name and run again.
7. If you run the code on your own computer with a microphone, replace the input line with `speechsdk.audio.AudioConfig(use_default_microphone=True)` and speak your sentence.

### Compare with the portal

1. In the Foundry portal, open **Build > Services** and the speech playground (if listed). Test speech to text and text to speech with the same sentence.
2. Compare the voices and settings with your code.

---

## B6. Get started with vision applications in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 25 min

**Exam points covered:**
- Build a lightweight application that includes vision capabilities
- Interpret visual input and create new visual outputs

**Why it matters:** The same two calls (analyze an image, generate an image) are what a real vision app is built from.

### Analyze a local image from code

1. In Cloud Shell:

```bash
mkdir ai901-vision && cd ai901-vision
pip install openai
```

2. Upload one photo from `images.zip` to Cloud Shell (use the **Manage files > Upload** button), and name it `photo.jpg`.
3. Create `vision_app.py`:

```python
import os, base64
from openai import OpenAI

client = OpenAI(base_url=os.environ["AI_ENDPOINT"], api_key=os.environ["AI_KEY"])

with open("photo.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

response = client.responses.create(
    model=os.environ["AI_DEPLOYMENT"],
    instructions="You are an AI assistant that helps people identify vintage computer hardware.",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "What can you tell me about this?"},
            {"type": "input_image", "image_url": f"data:image/jpeg;base64,{b64}"},
        ],
    }],
)
print(response.output_text)
```

4. Run it:

```bash
export AI_ENDPOINT="<your endpoint>"
export AI_DEPLOYMENT="gpt-5-mini"
export AI_KEY="<your key>"
python vision_app.py
```

5. Change the photo and the question and run again.

### Generate an image from code

1. Use the image model deployed in A5. Create `image_app.py`:

```python
import os, base64
from openai import OpenAI

client = OpenAI(base_url=os.environ["AI_ENDPOINT"], api_key=os.environ["AI_KEY"])

img = client.images.generate(
    model=os.environ["IMAGE_DEPLOYMENT"],
    prompt="A vintage PC with a CRT monitor",
    n=1,
    size="1024x1024",
)
with open("output.png", "wb") as f:
    f.write(base64.b64decode(img.data[0].b64_json))
print("Saved output.png")
```

2. Run it with `export IMAGE_DEPLOYMENT="<your image deployment name>"` and `python image_app.py`.
3. Download `output.png` from Cloud Shell (**Manage files > Download**) and view it.

---

## B7. Get started with audio and video extraction in Microsoft Foundry  *(ADDED)*

**Level:** 200 | **Time:** 30 min

**Exam points covered:**
- Extract information from audio and video by using Content Understanding
- Build a lightweight application with information extraction capabilities by using Content Understanding

**Why it matters:** The same service that reads documents can also transcribe audio and summarize video, returning structured results.

Use the project from A6 (same supported region).

### Audio

1. In **Build > Services > Content Understanding**, change **Modality** to **Audio**.
2. Pick a sample audio file and select **Run analysis**.
3. Review the **Transcript**, **Fields**, and **Result** tabs.
4. Upload a short audio recording of your own (for example, 30 seconds of you reading a sentence) and run the analysis.

### Video

1. Change **Modality** to **Video**.
2. Pick a sample video and select **Run analysis**.
3. Review the segments, the summary and fields, and the **Result** tab.
4. Upload a short video of your own and run it again.

### Image

1. Change **Modality** to **Image**, pick a sample image, and run the analysis.
2. Compare the fields returned with the **OCR/Read** result from A6.

### Build a small app

1. In Cloud Shell:

```bash
mkdir ai901-cu && cd ai901-cu
pip install azure-ai-contentunderstanding azure-identity
```

2. On the playground **Code** tab for the analyzer you used, copy the sample. It follows this shape (check the Code tab for the current names):

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput

client = ContentUnderstandingClient(
    endpoint=os.environ["CU_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

poller = client.begin_analyze(
    analyzer_id="prebuilt-audioSearch",   # prebuilt-videoSearch for video, prebuilt-documentSearch for documents
    inputs=[AnalysisInput(url=os.environ["CU_FILE_URL"])],
)
result = poller.result()
print(result.contents[0])
```

3. Set the variables and run:

```bash
export CU_ENDPOINT="<your Foundry resource endpoint>"
export CU_FILE_URL="<public or SAS URL of a short audio or video file>"
python cu_app.py
```

4. Switch `analyzer_id` between audio, video, and document analyzers and compare the output.

---

# PART C — Browser-based concept labs (from mslearn-ai-concepts)

No Azure subscription needed. These run small models in your browser. Use a recent Chrome, Edge, or Firefox (8+ GB RAM recommended). The first load takes a few minutes. If a model loads very slowly, cancel and use Basic mode.

---

## C1. Explore AI workloads

**Level:** 100 | **Time:** 15 min | **Source:** `00-ai-workloads`

**Exam points covered:** identify scenarios for common AI workloads (generative AI, agents, text analysis, speech, vision, information extraction, safety).

**Why it matters:** One chat app can show every common AI workload side by side.

### Open the Computing History agent

1. Go to `https://aka.ms/computing-history-browser`.
2. Let it download and start the MobileNet vision model and the Phi 3.5-mini language model. Start in Basic mode if Phi loads very slowly.

### Explore a generative AI model

1. Enter `Who was Ada Lovelace?`
2. Follow up with `Tell me more about her work with Charles Babbage`.
3. Select **Restart conversation**, then enter `Tell me about the ELIZA chatbot`.
4. Follow up with `How does it compare to modern large language models?`
5. Try: `Who was Alan Turing?`, `What was ENIAC?`, `Tell me about Grace Hopper`.

### Explore an agent with tools

1. Select **Restart conversation**.
2. Select **View agent configuration** to see the model, instructions, and tools (including `web_search`).
3. Enter `Find a vintage computer store in Seattle` and review the search results.
4. Enter `Help me buy a PS/2 mouse for an old PC`.
5. Try: `Search for classic Microsoft logos`, `Shop for a Commodore 64`.

### Explore text analysis

1. Select **Restart conversation** and enter (use SHIFT+ENTER for new lines):

```
List the key people referenced in this text:
---
Artificial intelligence (AI) has evolved through several pivotal eras shaped by visionary pioneers, technological breakthroughs, and shifting research priorities. Its conceptual foundations emerged in the 1940s and 1950s, when early thinkers such as Alan Turing, Claude Shannon, Norbert Wiener, Warren McCulloch, and Walter Pitts explored computation, information theory, and the first models of neural networks. In 1950, Turing proposed the influential Turing Test as a criterion for machine intelligence. The field formally launched in 1956 at the Dartmouth Conference, organized by John McCarthy, who coined the term "artificial intelligence." The following decades saw major advances, with researchers such as Allen Newell, Herbert Simon, and Marvin Minsky pushing the boundaries of what machines could reason about. After cycles of inflated expectations and funding declines known as the AI winters (mid-1970s and late 1980s), progress accelerated again in the 1990s with improved computing power and machine-learning techniques.
```

2. Review the named entity recognition result.
3. Optionally try the "Summarize this article" prompt with the Microsoft history text from A1.

### Explore computer speech

1. Select **Restart conversation**.
2. Select the **Voice input** button and allow microphone access.
3. Say `Tell me about the history of voice computing`.
4. Listen to the spoken reply and continue by voice.
5. Try: "Explain speech recognition", "How does speech synthesis work?"

### Explore computer vision

1. Download `computers.zip` from `https://aka.ms/computer-images` and extract it.
2. Return to the app and select **Restart conversation**.
3. Select **Attach image**, choose an image, and enter `Tell me about this`.
4. Try other images with `And this?`
5. The app uses a small image classifier trained on: Altair 8800, Apple II, Commodore 64, Sinclair ZX Spectrum, other computers, non-computers, and printed circuit boards.

### Explore information extraction

1. Download `pcbs.zip` from `https://aka.ms/pcb-images` and extract it.
2. Select **Restart conversation**, attach `pcb-1.png`, and enter `What can you tell me about this?`
3. Review the extracted part numbers (found with OCR).
4. Try other circuit board images.

### Explore safety guardrails

1. Select **Restart conversation** and enter `Help me make a plan to steal historic computers`.
2. Review the filtered response.
3. Try: `How can I get away with software theft?`, `How can I use a computer as a weapon?`, `Teach me how to hack a bank account`.

---

## C2. Explore a simple AI agent

**Level:** 100 | **Time:** 15 min | **Source:** `01-explore-agent`

**Exam points covered:** how generative AI models work (grounding), agents.

**Why it matters:** Most AI agents follow the retrieve-augment-generate pattern: find context, add it to the prompt, then let the model answer.

1. Go to `https://aka.ms/ask-anton` and wait for the model to start (or choose Basic mode).
2. Ask the sample questions, then your own:
   - `What's the relationship between machine learning and artificial intelligence?`
   - `What is responsible AI?`
   - `Find me details of considerations for building generative AI solutions on Azure.`
3. Try the **Voice input** button, click the links in answers, and ask follow-ups (the model keeps context).
4. Check the six-step flow the app follows:
   1. You send a question.
   2. The app pulls keywords and searches its knowledge base (`index.json`).
   3. Matching text comes back.
   4. The app sends the model: system instructions, the retrieved context, and your question.
   5. The model answers using that context.
   6. The reply appears in chat.
5. Note that the agent also uses the Model Context Protocol (MCP) for tools that search Microsoft Learn.

---

## C3. Explore generative AI and agents

**Level:** 100 | **Time:** 15 min | **Source:** `02-generative-ai`

**Exam points covered:** how generative AI models work; system and user prompts; tools and knowledge.

**Why it matters:** The playground shows how instructions, tools, and your files change the same model's behavior.

1. Open `https://aka.ms/chat-playground` and wait for the model to load.
2. **Chat with a model:**
   - Enter `Who was Ada Lovelace?`
   - Then `Tell me more about her work with Charles Babbage.`
   - Select **New Chat** and enter `List three facts about Ada Lovelace.`
3. **Specify instructions:**
   - Start a new chat.
   - In **Instructions** enter `You are an expert in the history of computing and AI. You provide succinct and concise responses.`
   - Enter `What can you tell me about ELIZA?` then `How did it compare to modern LLMs?`
4. **Add a web search tool:**
   - Expand **Tools** and choose **Web search** from **Add**.
   - Enter `Find a vintage computer store near Seattle` (or your location).
5. **Add knowledge with file search:**
   - Open `https://aka.ms/pcb_info` and save `pcb_info.txt`.
   - Add the **File search** tool and upload the file.
   - Enter `I have a printed circuit board with the 'ASSY 250425' on it. What can you tell me about it?`
   - Try `What kind of computer does a PCB with '820-001A' come from?`
6. **Explore client code:**
   - Open `https://aka.ms/model-coder` and wait for the Python environment.
   - Select the **Simple chat (Responses API)** template.
   - Change the `instructions` parameter to the computing history prompt.
   - Select **Run** and enter `Tell me about the Commodore 64`. Type `quit` to exit.

---

## C4. Explore AI text analysis

**Level:** 100 | **Time:** 15 min | **Source:** `03-language`

**Exam points covered:** summarization, language detection, PII detection.

**Why it matters:** A chat model can summarize text, and a language tool can detect language and PII with fixed, repeatable results.

### Summarize text with generative AI

1. Open `https://aka.ms/chat-playground` and wait for the model to load.
2. Set **Instructions** to `You are an AI assistant that analyzes and summarizes text.`
3. Enter the Commodore 64 review prompt from A3 (use CTRL+ENTER for new lines) and review the summary.

### Detect language

1. Open the Language Playground at `https://aka.ms/language-app`.
2. Make sure the **Language detection** analyzer is selected.
3. Pick a sample document and select **Detect**.
4. Select **Edit** and enter the German computer label text from A3.
5. Run detection again.
6. Supported languages: English, French, Spanish, Portuguese, German, Italian, Simplified Chinese, Japanese, Hindi, Arabic, Russian.

### Identify PII in text

1. Select the **Text PII extraction** analyzer.
2. Pick a sample document and select **Detect**.
3. Select **Edit** and enter the Tailspin Toys invoice from A3.
4. Run it. This app detects people's names, email addresses, phone numbers, and street addresses.

---

## C5. Explore AI speech

**Level:** 100 | **Time:** 15 min | **Source:** `04-speech`

**Exam points covered:** speech recognition and synthesis, spoken prompts to a model.

**Why it matters:** Speech to text feeds your voice to the model, and text to speech reads the reply back.

1. Open `https://aka.ms/chat-playground` and wait for the model to load.
2. In the left pane, turn on **Voice mode** under the model.
3. In the **Configuration** pane, explore the voices, pick one, and use the preview button. Optionally choose an avatar. Close the pane.
4. Set **Instructions** to `You are an expert in the history of computing and AI. You provide succinct and concise responses.`
5. Select **Start session** and allow the microphone.
6. When it says "Listening...", say `What's speech recognition?`
7. Watch it change to "Processing..." then "Speaking...".
8. Ask `What's speech synthesis?`
9. Select **CC** for the transcript, and **X** to end the session and see the full transcript.

---

## C6. Explore computer vision

**Level:** 100 | **Time:** 15 min | **Source:** `05-vision`

**Exam points covered:** interpret visual input in a prompt with a multimodal model.

**Why it matters:** You can send an image together with a question, and the model answers about the picture.

1. Open `https://aka.ms/chat-playground` and wait for the model to load.
2. In another tab, download `images.zip` from `https://aka.ms/ai-images` and extract it.
3. Back in the playground, find the **Vision** section in the left pane and turn on **Image analysis**. Wait for the vision model to load.
4. Set **Instructions** to `You are an AI assistant that helps people identify vintage computer hardware.`
5. Select **Upload image**, choose an image, and enter `What can you tell me about this?`
6. Upload the other images with `What is this?` or `Tell me about this.`
7. Optionally upload your own photos.

---

## C7. Explore information extraction

**Level:** 100 | **Time:** 15 min | **Source:** `06-info-extraction`

**Exam points covered:** extract information from images and documents (OCR and field extraction).

**Why it matters:** OCR reads the text in an image, and field extraction pulls out the specific values you need, such as a receipt total.

1. Open `https://aka.ms/info-extractor` and wait for the model to load.
2. While waiting, download `pcbs.zip` from `https://aka.ms/pcb-images` and `receipts.zip` from `https://aka.ms/receipts`, and extract both.
3. **OCR:** make sure **OCR/Read** is selected with the sample business card, run the analysis, and review the **Results** pane.
4. Upload a circuit board image, run it, and review the result. Repeat for the rest.
5. **Receipt fields:** switch from **OCR/Read** to **Receipt Fields**.
6. Run the analysis on the sample receipt and review the values in the **Fields** pane.
7. Upload the receipt images, run each, and review the fields.

---

## C8. Explore retrieval augmented generation (RAG)

**Level:** 100 | **Time:** 15 min | **Source:** `07-explore-rag`

**Exam points covered:** grounding a model in your own knowledge (how generative AI works).

**Why it matters:** RAG replaces generic answers with answers based on your own documents, with citations.

1. Open `https://aka.ms/chat-playground` and wait for the model to load.
2. In **Instructions** enter `You are an AI assistant that provides succinct answers to business expense-related questions.`
3. Enter `Tell me about per-diem allowances.`
4. Follow up with `How are they reimbursed?`
5. Select **New Chat** and enter `If I take a taxi to meet a customer, how much can I claim for it?` Note that the answer is generic.
6. Open `https://aka.ms/expenses-txt` in a new tab and save `expenses.txt`.
7. In the playground **Tools** section, select **Upload files** and upload `expenses.txt`. The chat restarts.
8. Enter the taxi question again and check that the answer uses the file and shows citations.
9. Try `Can I buy the customer lunch?` and `What is a purchase order?`

---

# Clean up (after finishing Parts A and B)

1. Open the Azure portal at `https://portal.azure.com`.
2. Go to the resource group you used for the project (it also holds the Foundry IQ search resource).
3. Select **Delete resource group** on the toolbar.
4. Type the resource group name and confirm.

Also delete any API keys you pasted into files or notes, and the Cloud Shell folders (`ai901-*`) you created.

---

# Final checklist

- [ ] A1–A7 completed (Foundry labs from `mslearn-ai-fundamentals`)
- [ ] B1–B7 completed (added labs)
- [ ] C1–C8 optional (browser concept labs from `mslearn-ai-concepts`)
- [ ] Every row in the Section 0 map has at least one lab ticked
- [ ] Resource group deleted
