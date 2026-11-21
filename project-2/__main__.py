from src.model import run_model


def main():

    # start running software
    while True:
        user_input = input("User (exit with \"bye\"): ")
        if user_input.lower() == "bye":
            break
        # user defined task
        user_task = {"role": "user", "content": user_input}
        # Agent output
        output = run_model(user_role=user_task)
        print(output)


if __name__ == "__main__":
    main()
