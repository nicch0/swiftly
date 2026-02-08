from langchain.agents import create_agent
from venv import create
import getpass
import os
from dataclasses import dataclass
from langchain.chat_models import init_chat_model
from langchain.agents.structured_output import ToolStrategy
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import InMemorySaver
import getpass
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT ="""
You are a helpful assistant.
"""

MODEL = "claude-haiku-4-5"

checkpointer = InMemorySaver()

# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

# Define context schema
@dataclass
class Context:
    """Custom runtime context schema."""
    user_name: str

context = Context(user_name="Nick")

model = init_chat_model(
    MODEL,
    temperature=1.0,
)

cerebro = create_agent(
  model=model,
  tools=[],
  system_prompt=SYSTEM_PROMPT,
  context_schema=Context,
  checkpointer=checkpointer,
)

def main():
  while True:
    user_input = input(">>>> ")

    # Run the agent
    stream_response = cerebro.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        {"configurable": {"thread_id": "1"}},
        context=context,
        stream_mode="messages",
    )

    for token, metadata in stream_response:
      if token.content_blocks and token.content_blocks[-1] and token.content_blocks[-1]["type"] == "text":
        chunk = token.content_blocks[-1]["text"]
        print(chunk, end="")

    print("\n")


if __name__ == "__main__":
    main()
