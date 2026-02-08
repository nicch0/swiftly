from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

load_dotenv()

MODEL = "claude-haiku-4-5"

DB_URI = "postgresql://niccho@localhost:5432/postgres?sslmode=disable"

# Collect learnings from ./learnings directory
def load_learnings():
    learnings_dir = Path("./learnings")
    if not learnings_dir.exists():
        return ""

    learnings_content = []
    for file_path in learnings_dir.rglob("*"):
        if file_path.is_file() and file_path.suffix in [".md"]:
            try:
                content = file_path.read_text()
                learnings_content.append(f"## From {file_path.name}\n{content}")
            except Exception:
                pass

    if learnings_content:
        return "\n\n# Knowledge Base\n" + "\n\n".join(learnings_content)
    return ""

learnings_content = load_learnings()

SYSTEM_PROMPT = """
You are Swiftly. An autonomous AI agent whose goal is to ensure that the user learns and understands
new concepts, procedures, and facts. You are an expert in coaching users and follow the best science
-based learning practices including mastery learning, spaced repetition, deliberate practice,
amongst other techniques.
"""

# Create learnings message to be added to conversation
learnings_messages = []
if learnings_content:
    learnings_messages = [
        {
            "role": "user",
            "content": f"Here is my knowledge base for reference:\n\n{learnings_content}",
        },
        {
            "role": "assistant",
            "content": "I've reviewed your knowledge base and will use it to inform my responses.",
        },
    ]

model = init_chat_model(
    MODEL,
    temperature=1.0,
)

swiftly = create_agent(
    model=model,
    tools=[],
    system_prompt=SYSTEM_PROMPT,
)
