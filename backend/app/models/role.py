from enum import Enum
from pydantic import BaseModel, Field

class Role(str, Enum):
    admin = "admin"
    user = "user"