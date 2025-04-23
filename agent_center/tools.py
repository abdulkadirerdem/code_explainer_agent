from typing import List, Dict, Any
from agents import function_tool


from core.function_selector import select_key_functions
from core.summarizer import summarize_function
from core.input_loader import load_dummy_input
from agent_center.types import FunctionInfo


@function_tool(strict_mode=False)
def select_important_functions_tool(
    functions: List[FunctionInfo], top_n: int = 3
) -> List[FunctionInfo]:
    return select_key_functions(functions, top_n=top_n)


@function_tool(strict_mode=False)
def summarize_function_tool(function: FunctionInfo) -> str:
    return summarize_function(function)


@function_tool(strict_mode=False)
def load_dummy_input_tool(file_path: str) -> Dict[str, Any]:
    return load_dummy_input(file_path)
