from src import CONFIG, LLM_ROLE
from src.llm_util import perform_task


def main():
    # user defined task
    my_task = "Run a Genome Wide Association Study."

    # provide LLM with specified task
    result = perform_task(
        llm_role=LLM_ROLE,
        model=CONFIG["model"],
        task=my_task,
    )

    print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
