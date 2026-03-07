from pydantic import BaseModel


class CommandRequest(BaseModel):
    query: str


class FolderRequest(BaseModel):
    path: str
