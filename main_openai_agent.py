import argparse
from agents import Runner
from core.input_loader import load_dummy_input
from agent_center.openai_agent import code_explainer_agent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the OpenAI Agent with a prompt and input file."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="examples/dummy_input.json",
        help="Path to dummy input JSON",
    )

    args = parser.parse_args()

    print(
        "🧠 Give a task to the Agent, for example:"
        "\n- What does this agent do?"
        "\n- Analyze and explain the most important functions in the file. File path: examples/dummy_input.json"
        "\n- Scan the examples/dummy_input.json file and comment on the functions."
    )
    user_input = input("📝 Prompt: ")

    result = Runner.run_sync(code_explainer_agent, user_input)

    print("\n✅ Final Output:\n")
    print(result.final_output)
    
    # Save the output to a file
    with open("outputs/agent_response.md", "w") as f:
        f.write(result.final_output)
