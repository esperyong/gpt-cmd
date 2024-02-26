import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="CLI for interacting with GPT models, including image recognition and generation.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--image_recognition", type=str, help="Perform image recognition on the specified file path.", metavar="FILE")
    group.add_argument("--image_generation", type=str, help="Generate an image based on the specified prompt.", metavar="PROMPT")
    group.add_argument("--no_markdown", action="store_true", help="Disable markdown formatting in the chat session.")
    group.add_argument("--model", type=str, help="The model to use for the chat session. Overrides the default model defined for the assistant.")
    group.add_argument("--temperature", type=float, help="The temperature to use for the chat session. Overrides the default temperature defined for the assistant.")
    group.add_argument("--top_p", type=float, help="The top_p to use for the chat session. Overrides the default top_p defined for the assistant.")
    group.add_argument("--log_file", type=str, help="The file to write logs to. Supports strftime format codes.")
    group.add_argument("--log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="The log level to use")
    group.add_argument("--prompt", "-p", type=str, action="append", help="If specified, will not start an interactive chat session and instead will print the response to standard output and exit. May be specified multiple times. Use `-` to read the prompt from standard input. Implies --no_markdown.")
    group.add_argument("--execute", "-e", type=str, help="If specified, passes the prompt to the assistant and allows the user to edit the produced shell command before executing it. Implies --no_stream. Use `-` to read the prompt from standard input.")
    group.add_argument("--no_stream", action="store_true", help="If specified, will not stream the response to standard output. This is useful if you want to use the response in a script. Ignored when the --prompt option is not specified.")
    group.add_argument("--no_price", action="store_true", help="Disable price logging.")
    return parser.parse_args()
