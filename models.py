from pydantic import BaseModel, ConfigDict


class TaskAdd(BaseModel):
    name:str
    description: str|None=None

class TaskRead(TaskAdd):
    id:int
    model_config = ConfigDict(from_attributes=True)

class TaskId(BaseModel):
    id:int
    status:bool=True