from pydantic import BaseModel
from pydantic.networks import AnyHttpUrl
from enum import Enum
from typing import Union, Literal


class ParagraphData(BaseModel):
    text: str


class ParagraphElement(BaseModel):
    type: Literal["paragraph"]
    data: ParagraphData


class HeaderData(BaseModel):
    text: str
    level: int


class HeaderElement(BaseModel):
    type: Literal["header"]
    data: HeaderData


class ListData(BaseModel):
    style: str
    items: list[str]


class ListElement(BaseModel):
    type: Literal["list"]
    data: ListData


Element = Union[
    HeaderElement,
    ListData,
    ListElement,
]


class Document(BaseModel):
    name: str
    content: list[Element]
    style: str


class RenderedDocument(BaseModel):
    url: AnyHttpUrl
