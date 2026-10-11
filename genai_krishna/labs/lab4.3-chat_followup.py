"""
Lab 4.3 - Keep a conversation going

The model has no memory. Each call is like phoning a help desk and
getting a new person. To continue a conversation you quote the
"ticket number" of the previous answer:

    first.id                      -> the ticket number of turn 1
    previous_response_id=first.id -> quoting that ticket in turn 2

Azure then loads turn 1 and sends it to the model with the new question.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------------------
# SETTINGS - the only lines you change
# ---------------------------------------------------------------
USE_LINK = True   # True  = turn 2 remembers turn 1
                  # False = turn 2 knows nothing (use this to prove the link matters)

QUESTION_1 = "Define a private endpoint in one sentence."
QUESTION_2 = "Now explain it to a college freshman."

# A stronger test - swap these in to try a fact the model cannot guess:
# QUESTION_1 = "My secret code is BLUE-742. Just say OK."
# QUESTION_2 = "What is my secret code?"

# ---------------------------------------------------------------
# CONNECT - values come from .env
# ---------------------------------------------------------------
load_dotenv()
client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_BASE_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
MODEL = os.environ["CHAT_DEPLOYMENT"]

# ---------------------------------------------------------------
# TURN 1 - a normal question
# ---------------------------------------------------------------
first = client.responses.create(
    model=MODEL,
    input=QUESTION_1,
)

# ---------------------------------------------------------------
# TURN 2 - the follow-up
# ---------------------------------------------------------------
second = client.responses.create(
    model=MODEL,
    previous_response_id=first.id if USE_LINK else None,   # the link to turn 1
    input=QUESTION_2,
)

# ---------------------------------------------------------------
# SHOW THE CONVERSATION
# ---------------------------------------------------------------
print("You   :", QUESTION_1)
print("Model :", first.output_text)
print()
print("You   :", QUESTION_2)
print("Model :", second.output_text)

# ---------------------------------------------------------------
# PROOF - evidence that turn 2 used turn 1
# ---------------------------------------------------------------
print()
print("----- proof -----")
print("Link used            :", USE_LINK)
print("Turn 1 ID            :", first.id)
print("Turn 2 is linked to  :", second.previous_response_id)   # same as Turn 1 ID when linked
print("Turn 1 input tokens  :", first.usage.input_tokens)
print("Turn 2 input tokens  :", second.usage.input_tokens)      # much higher when linked
