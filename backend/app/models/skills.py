from pydantic import BaseModel, Field
from typing import Optional
from typing import List

class Skills(BaseModel):
    skills: Optional[List[str]] = None