from typing_extensions import TypedDict
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class FunctionInfo(TypedDict):
    name: str
    code: str
    docstring: str
    fan_in: int
    fan_out: int
    is_entry_point: bool

class FunctionSummary(BaseModel):
    """Summary information for a single function"""

    name: str = Field(description="Function name")
    purpose: str = Field(description="Function purpose summary")
    key_features: List[str] = Field(description="Key aspects of the function")


class FinalResponse(BaseModel):
    """Final output of the code explainer chain"""

    summaries: List[FunctionSummary] = Field(
        description="Summaries of analyzed functions"
    )
    overall_analysis: str = Field(description="Overall analysis of the code")
