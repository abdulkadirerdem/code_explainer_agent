from typing_extensions import TypedDict


class FunctionInfo(TypedDict):
    name: str
    code: str
    docstring: str
    fan_in: int
    fan_out: int
    is_entry_point: bool 