from datetime import date

from langchain.tools import tool

from src import config


@tool
def get_current_date() -> str:
    """Get the current date in ISO format (YYYY-MM-DD)."""
    return date.today().isoformat()


@tool
def change_model_to_sonnet() -> str:
    """Switch the AI model to Claude Sonnet 4.5 for more capable responses.

    Use this when you need deeper reasoning or more nuanced answers.
    The change takes effect on the next conversation turn.
    """
    config.MODEL = "claude-sonnet-4-5-20250929"
    return "Model switched to Claude Sonnet 4.5. Change takes effect on the next turn."
