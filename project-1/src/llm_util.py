import ollama
from pydantic import BaseModel, Field


class TaskReview(BaseModel):
    """ Review of the structured response by the LLM. """

    task: str = Field(
        description="A clear and precise description of the task."
    )

    interpretation: str = Field(
        description="A simple description of what the task requires."
    )

    steps: list[str] = Field(
        description="A list of the steps necessary to achieve the goal of the task."
    )

    needs_clarification: bool = Field(
        description="Set to True if information essential to the task is missing."
    )


def perform_task(llm_role: dict, task: str, model: str) -> TaskReview:
    """ Uses a specified LLM model to review and perform the user-specified task. """
    # user's task formatted for LLM
    user_role = {
        "role": "user",
        "content": task
    }
    # message formatted for LLM
    messages =[
        llm_role,
        user_role,
    ]
    # get response from LLM
    raw_response = ollama.chat(
        model=model,
        messages=messages,
        format=TaskReview.model_json_schema(),
        options={"temperature": 0},
    )
    # format response
    response = TaskReview.model_validate_json(raw_response.message.content)

    return response
