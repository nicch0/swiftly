from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.tools.file_operations import list_directory, read_markdown_file, write_markdown_file
from src.system_prompt import SYSTEM_PROMPT

load_dotenv()

MODEL = "claude-haiku-4-5"


model = init_chat_model(
    MODEL,
    temperature=1.0,
)

swiftly = create_agent(
    model=model,
    tools=[read_markdown_file, write_markdown_file, list_directory],
    system_prompt=SYSTEM_PROMPT,
)
