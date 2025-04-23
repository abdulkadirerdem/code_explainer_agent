import argparse
from core.input_loader import load_dummy_input
from core.function_selector import select_key_functions
from core.summarizer import summarize_function
from core.formatter import format_as_json, format_as_markdown
import os


def run_pipeline(input_path: str, top_n: int, output_dir: str = "outputs"):
    print("🚀 Loading input...")
    data = load_dummy_input(input_path)
    file_name = data["file"]
    functions = data["functions"]

    print(f"🔍 Selecting top {top_n} functions...")
    selected = select_key_functions(functions, top_n=top_n)

    summarized = []
    for fn in selected:
        print(f"🧠 Summarizing `{fn['name']}`...")
        explanation = summarize_function(fn)
        summarized.append(
            {"name": fn["name"], "code": fn["code"], "explanation": explanation}
        )

    print("📦 Formatting outputs...")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "run_output.json"), "w", encoding="utf-8") as f:
        f.write(format_as_json(file_name, summarized))

    with open(os.path.join(output_dir, "doc_output.md"), "w", encoding="utf-8") as f:
        f.write(format_as_markdown(file_name, summarized))

    print("✅ All done! Outputs saved in:", output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM-Powered Code Summarizer")
    parser.add_argument(
        "--path",
        type=str,
        default="examples/dummy_input.json",
        help="Path to input JSON",
    )
    parser.add_argument(
        "--top_n", type=int, default=3, help="Number of top functions to summarize"
    )

    args = parser.parse_args()
    run_pipeline(args.path, args.top_n)
