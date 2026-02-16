from datetime import date

from langchain.tools import tool


@tool
def get_current_date() -> str:
    """Get the current date in ISO format (YYYY-MM-DD)."""
    return date.today().isoformat()
