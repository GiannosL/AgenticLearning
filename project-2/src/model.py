import ollama
from src import CONFIG, read_file, parse_image

def run_model(user_role: dict) -> str:
    # message
    messages = [CONFIG["llm_role"], user_role]

    #
    response = ollama.chat(
        model=CONFIG["model"],
        messages=messages,
        tools=CONFIG["tool_list"],
        think=True,
    )
    print(response.message)
    # add assistant message to messages
    messages.append(response.message)
    if response.message.tool_calls:
        # iterate if there are multiple tool calls
        for my_call in response.message.tool_calls:
            if my_call.function.name == "read_file":
                my_result = read_file(**my_call.function.arguments)
            if my_call.function.name == "parse_image":
                my_result = parse_image(**my_call.function.arguments)

            #add the tool output to the messages
            messages.append({"role": "tool", "tool_name": my_call.function.name, "content": str(my_result)})

        final_response = ollama.chat(
            model=CONFIG["model"],
            messages=messages,
            tools=CONFIG["tool_list"],
            think=True,
        )
    print("============================================================")
    for mess in messages:
        print(mess)
    print("============================================================")
    print(final_response)
    print("-------------------------------------------------------------------------")

    return final_response.message.content
