from PIL import Image
from pathlib import Path


def read_file(file_name: str) -> str:
    #
    file_path = Path(file_name)

    if file_path.exists():
        with open(file_path, "r") as f:
            contents = f.read()

        return contents
    else:
        raise ValueError("File does not exist. Please check file path.")


def parse_image(file_name: str):
    #
    file_path = Path(file_name)

    if file_path.exists():
        return Image.open(file_name)
    else:
        raise ValueError("File does not exist. Please check file path.")



CONFIG = {
    "model": "qwen3.5:9b",
    "tool_list": [read_file, parse_image],
    "llm_role": {
        "role": "system",
        "content": (
            "You are an AI assistant that breaks down user tasks. "
            "When you receive input, identify the task, interpret "
            "what the task asks you to do, and break the task down "
            "into steps. If information essential to the task is "
            "missing, indicate that clarification is necessary."
        ),
    }
}
