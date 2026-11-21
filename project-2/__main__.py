from src.model import run_model


def main():
    user_input = input("User input of LLM: ")

    user_task = {"role": "user", "content": str(user_input)}

    output = run_model(user_role=user_task)

    print(f"\n{output}")


if __name__ == "__main__":
    main()
