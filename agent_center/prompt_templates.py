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
