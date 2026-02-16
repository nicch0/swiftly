from pathlib import Path

from langchain.tools import tool


@tool
def read_markdown_file(file_path: str) -> str:
    """Read a markdown file and return its contents.

    Args:
        file_path: Path to the markdown file (absolute or relative to project root)

    Returns:
        The file contents as a string
    """
    try:
        path = Path(file_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        return path.read_text()
    except FileNotFoundError:
        return f"Error: File not found: {file_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

@tool
def write_markdown_file(file_path: str, content: str) -> str:
    """Write content to a markdown file, creating it if it doesn't exist.

    Args:
        file_path: Path to the markdown file (absolute or relative to project root)
        content: The content to write to the file

    Returns:
        Success message
    """
    try:
        path = Path(file_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"


@tool
def list_directory(directory_path: str) -> str:
    """List contents of a directory.

    Args:
        directory_path: Path to the directory (absolute or relative to project root)

    Returns:
        Formatted list of files and directories
    """
    try:
        path = Path(directory_path)
        if not path.is_absolute():
            path = Path.cwd() / path

        if not path.exists():
            return f"Error: Directory not found: {directory_path}"

        if not path.is_dir():
            return f"Error: {directory_path} is not a directory"

        items = []
        for item in sorted(path.iterdir()):
            if item.is_dir():
                items.append(f"📁 {item.name}/")
            else:
                items.append(f"📄 {item.name}")

        if not items:
            return f"Directory {directory_path} is empty"

        return f"Contents of {directory_path}:\n" + "\n".join(items)
    except Exception as e:
        return f"Error listing directory: {str(e)}"
