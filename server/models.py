# This file contains definitions for database tables and relationships
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False, unique=True)
    # email_address = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    full_name = Column(String(50), nullable=False)

    user_condition = relationship("UserCondition", back_populates="user")
    post = relationship("Post", back_populates="user")


class Condition(Base):
    __tablename__ = "condition"
    condition_id = Column(Integer, primary_key=True, index=True)
    condition_name = Column(String(50), nullable=False, unique=True)

    user_condition = relationship("UserCondition", back_populates="condition")


class UserCondition(Base):
    __tablename__ = "user_condition"
    user_condition_id = Column(Integer, primary_key=True, index=True)
    condition_id = Column(Integer, ForeignKey("condition.condition_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))

    user = relationship("User", back_populates="user_condition")
    condition = relationship("Condition", back_populates="user_condition")


class Message(Base):
    __tablename__ = "message"
    message_id = Column(Integer, primary_key=True, index=True)
    content = Column(String(65535), nullable=False)  # MAX
    timestamp = Column(DateTime(), nullable=False)
    from_user_id = Column(Integer, ForeignKey("user.user_id"))
    to_user_id = Column(Integer, ForeignKey("user.user_id"))

    to_user = relationship("User", foreign_keys=[to_user_id])
    from_user = relationship("User", foreign_keys=[from_user_id])


class Forum(Base):
    __tablename__ = "forum"
    forum_id = Column(Integer, primary_key=True, index=True)
    forum_name = Column(String(50), nullable=False, unique=True)

    post = relationship("Post", back_populates="forum")


class Post(Base):
    __tablename__ = "post"
    post_id = Column(Integer, primary_key=True, index=True)
    content = Column(String(65535), nullable=False)  # MAX
    timestamp = Column(DateTime(), nullable=False)
    forum_id = Column(Integer, ForeignKey("forum.forum_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))

    forum = relationship("Forum", back_populates="post")
    user = relationship("User", back_populates="post")
    post_reply = relationship("PostReply", back_populates="post")


class PostReply(Base):
    __tablename__ = "post_reply"
    post_reply_id = Column(Integer, primary_key=True, index=True)
    content = Column(String(65535), nullable=False)  # MAX
    timestamp = Column(DateTime(), nullable=False)
    post_id = Column(Integer, ForeignKey("post.post_id"))
    parent_reply_id = Column(Integer, ForeignKey("post_reply.post_reply_id"), nullable=True)

    post = relationship("Post", back_populates="post_reply")
