# This file contains object definitions
from pydantic import BaseModel, validator
from typing import Optional, List
import datetime


class StrictBaseModel(BaseModel):
    class Config:
        extra = "forbid"


class User(BaseModel):
    user_name: str
    email_address: str
    password: str
    full_name: str


class Message(BaseModel):
    content: str
    timestamp: datetime.datetime
    to_user_id: int
    from_user_id: int


class Condition(BaseModel):
    condition_name: str


class Post(BaseModel):
    content: str
    timestamp: datetime.datetime
    forum_id: int
    user_id: int


class PostReply(BaseModel):
    content: str
    timestamp: datetime.datetime
    post_id: int
    parent_reply_id: Optional[int]
