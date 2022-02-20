import email
import string
from pydantic import BaseModel
from pyparsing import stringStart


class Blog(BaseModel):
    
    name:str
    email:str
    password:str