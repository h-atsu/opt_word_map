from pydantic import BaseModel


class OptTerm(BaseModel):
    term: str
    url: str
    list_related_term: list[str]
