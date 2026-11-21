import ollama
import inspect
from src import CONFIG, read_file, parse_image

def run_model(user_role: dict) -> str:
    """
    """
    # dynamic tool dispatch
    tool_dispatch = {tool.__name__: tool for tool in CONFIG["tool_list"]}
    # message
    messages = [CONFIG["llm_role"], user_role]

    #
    while True:
        response = ollama.chat(
            model=CONFIG["model"],
            messages=messages,
            tools=CONFIG["tool_list"],
            think=True,
        )
        # add assistant message to messages
        messages.append(response.message)

        if not response.message.tool_calls:
            return response.message.content

        # iterate if there are multiple tool calls
        for tool_call in response.message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = tool_call.function.arguments

            try:
                if tool_name not in tool_dispatch.keys():
                    return ValueError(f"Unknown tool: {tool_name}")

                # validate arguments against function signature
                tool_function = tool_dispatch[tool_name]
                signature = inspect.signature(tool_function)
                signature.bind(**tool_args)

                # execute tool
                result = tool_function(**tool_args)
            except Exception as e:
                result = f"Tool execution failed: {type(e).__name__}: {e}"

            #add the tool output to the messages
            messages.append({"role": "tool", "tool_name": tool_name, "content": str(result)})
