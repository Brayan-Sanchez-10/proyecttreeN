from pydantic import BaseModel
from model.location import Location
from model.typedoc import Typedoc

class Person(BaseModel):
    id: str
    parent_id: str
    name: str
    last_name: str
    age: int
    gender: str
    type_doc: Typedoc
    location: Location