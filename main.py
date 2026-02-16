
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from src import config
from src.system_prompt import SYSTEM_PROMPT
from src.tools.file_operations import list_directory, read_markdown_file, write_markdown_file
from src.tools.utilities import get_current_date

load_dotenv()


def create_swiftly():
    model = init_chat_model(
        config.MODEL,
        temperature=config.TEMPERATURE,
    )
    return create_agent(
        model=model,
        tools=[
            read_markdown_file,
            write_markdown_file,
            list_directory,
            get_current_date,
        ],
        system_prompt=SYSTEM_PROMPT,
    )


swiftly = create_swiftly()
