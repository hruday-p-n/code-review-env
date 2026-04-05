from pydantic import BaseModel
from typing import List, Optional

class FileDiff(BaseModel):
    filename: str
    diff: str

class Observation(BaseModel):
    pr_id: int
    files_changed: List[FileDiff]
    comments_so_far: List[str]
    step_count: int

class Action(BaseModel):
    action_type: str
    file: Optional[str] = None
    line: Optional[int] = None
    comment: Optional[str] = None

class Reward(BaseModel):
    value: float
    reason: str