from typing import Union, List
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import Column, String, Integer, Identity, Sequence, Float, Boolean, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Identity(start=10), primary_key=True)
    name = Column(String, index=True, nullable=False)
    hashed_password = Column(String)

class Tags(str, Enum):
    users = "users"
    advents = "advents"
    info = "info"
    good = "good"

class Person(BaseModel):
    lastName: str = Field(default="lastname", min_length=3, max_length=20)
    age: int = Field(default=100, ge=10, lt=200)

class Foto(BaseModel):
    url: HttpUrl
    name: Union[str, None] = None

class User_new(BaseModel):
    name: Union[str, None] = None
    id: int = Field(default=100, ge=10, lt=200)
    person: Union[Person, None] = None
    day_list0: List[str]
    day_list1: Union[List[str], None] = None
    day_list2: Union[List[int], None] = None
    foto_list: Union[List[Foto], None] = None

class Good(BaseModel):
    id: int = Field(default=100, ge=1, lt=200)
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = 0
    nalog: Union[float, None] = 13.6

class Main_User(BaseModel):
    id: int = Field(default=100, ge=1, lt=200)
    name: Union[str, None] = None

class Main_UserDB(Main_User):
    hashed_password: str = Field(max_length=200, min_length=6)

class New_Respons(BaseModel):
    message: str
