from typing import List
from agent_center.types import FunctionInfo


def function_summary_prompt_template(fn: FunctionInfo) -> str:
    return f"""
You are an expert Python developer and technical writer.

Your task is to analyze the following function and explain its purpose in simple terms.
Only write the explanation. Do not repeat the code.

---

Function Name: {fn['name']}
Docstring: {fn.get('docstring', 'N/A')}
Fan-in: {fn.get('fan_in')}
Fan-out: {fn.get('fan_out')}
Entry Point: {fn.get('is_entry_point')}

Code:
{fn['code']}
"""


def function_selection_prompt_template(functions: List[FunctionInfo], top_n: int = 3) -> str:
    """Generate a prompt to select the most important functions."""
    functions_info = "\n\n".join([
        f"Function Name: {fn['name']}\n"
        f"Docstring: {fn.get('docstring', 'N/A')}\n"
        f"Fan-in: {fn.get('fan_in')}\n"
        f"Fan-out: {fn.get('fan_out')}\n"
        f"Entry Point: {fn.get('is_entry_point')}\n"
        f"Code Preview: {fn['code'][:300]}..." if len(fn['code']) > 300 else fn['code']
        for fn in functions
    ])
    
    return f"""
You are an expert Python code analyzer.

Your task is to analyze a list of functions and select the {top_n} most important ones.
Consider factors like:
- Entry points to the codebase
- Functions with high fan-in or fan-out (called by many other functions or calls many functions)
- Functions that implement core business logic
- Functions with descriptive names and docstrings

Select the functions that would be most helpful to understand the codebase as a whole.

---

Functions to analyze:
{functions_info}
"""


def generate_overall_analysis_prompt(function_summaries: List[dict]) -> str:
    """Generate a prompt to create an overall analysis of the code."""
    summaries = "\n\n".join([
        f"Function: {summary['name']}\n"
        f"Purpose: {summary['purpose']}\n"
        f"Key Features: {', '.join(summary['key_features'])}"
        for summary in function_summaries
    ])
    
    return f"""
You are an expert software architect and code reviewer.

Based on the summaries of key functions below, provide an overall analysis of this codebase.
Consider:
- The main purpose of the code
- Architecture patterns used
- Quality of the implementation
- Potential areas for improvement

Your analysis should be concise but insightful.

---

Function Summaries:
{summaries}
"""
