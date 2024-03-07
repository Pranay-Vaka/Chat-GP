# This file manages the requests sent to the server and executes SQL commands
from fastapi import FastAPI, Depends, Response, status, HTTPException
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, update, and_, or_, delete, distinct
import random
import json
import string
import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():  # Used to get database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/login", status_code=status.HTTP_200_OK)
def login(username: str, password: str, db: Session = Depends(get_db)):
    statement = (
        select(models.User)
        .where(
            models.User.user_name == username,
            models.User.password == password
        )
    )
    try:
        user = db.scalars(statement).one()
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials.")

    return user


@app.post("/user/add", status_code=status.HTTP_200_OK)  # Add new user
def add_new_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        user_name=user.user_name,
        password=user.password,
        full_name=user.full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.post("/message", status_code=status.HTTP_200_OK)
def send_message(msg: schemas.Message, db: Session = Depends(get_db)):
    new_msg = models.Message(
        from_user_id=msg.from_user_id,
        content=msg.content,
        timestamp=msg.timestamp,
        to_user_id=msg.to_user_id
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)


@app.get("/message/list", status_code=status.HTTP_200_OK)
def get_chats(user_id: int, db: Session = Depends(get_db)):
    stmt = select(
        models.User.user_id,
        models.User.user_name
    ).where(
        or_(
            user_id == models.Message.to_user_id,
            user_id == models.Message.from_user_id
        ),
        or_(
            models.User.user_id == models.Message.to_user_id,
            models.User.user_id == models.Message.from_user_id
        )
    )

    message_list = db.execute(stmt)

    return [{"user_id": x[0], "user_name": x[1]} for x in message_list]


@app.get("/user", status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    stmt = select(
        models.User
    ).where(
        models.User.user_id == user_id
    )
    user = db.scalars(stmt).one()
    return user.user_name, user.full_name


@app.get("/message/all", status_code=status.HTTP_200_OK)
def get_messages(other_user_id: int, db: Session = Depends(get_db)):
    stmt = select(
        models.Message
    ).where(
        or_(
            models.Message.from_user_id == other_user_id,
            models.Message.to_user_id == other_user_id
        )
    ).distinct()

    messages = db.scalars(stmt).all()

    return messages


@app.post("/condition", status_code=status.HTTP_200_OK)
def add_disease(condition: schemas.Condition, db: Session = Depends(get_db)):
    new_condition = models.Condition(
        condition_name=condition.condition_name
    )
    db.add(new_condition)
    db.commit()
    db.refresh(new_condition)


@app.post("/user/condition", status_code=status.HTTP_200_OK)
def add_user_condition(user_id: int, condition_id: int, db: Session = Depends(get_db)):
    new_u_c = models.UserCondition(
        condition_id=condition_id,
        user_id=user_id
    )
    db.add(new_u_c)
    db.commit()
    db.refresh(new_u_c)


@app.post("/forum/post", status_code=status.HTTP_200_OK)
def add_new_forum_post(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(
        content=post.content,
        timestamp=post.timestamp,
        forum_id=post.forum_id,
        user_id=post.user_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)


@app.post("/forum/post/reply", status_code=status.HTTP_200_OK)
def add_post_reply(reply: schemas.PostReply, db: Session = Depends(get_db)):
    new_reply = models.PostReply(
        content=reply.content,
        timestamp=reply.timestamp,
        post_id=reply.post_id,
        parent_reply_id=reply.parent_reply_id
    )
    db.add(new_reply)
    db.commit()
    db.refresh(new_reply)


@app.post("/forum", status_code=status.HTTP_200_OK)
def create_forum(forum_name: str, db: Session = Depends(get_db)):
    forum = models.Forum(
        forum_name=forum_name
    )
    db.add(forum)
    db.commit()
    db.refresh(forum)


@app.get("/forum", status_code=status.HTTP_200_OK)
def get_forums(db: Session = Depends(get_db)):
    stmt = select(models.Forum)
    forums = db.scalars(stmt).all()
    return forums


@app.get("/forum/post", status_code=status.HTTP_200_OK)
def get_forum_posts(forum_id: int, db: Session = Depends(get_db)):
    stmt = (
        select(models.Post)
        .join(models.Forum)
        .where(
            models.Forum.forum_id == forum_id
        )
    )

    posts = db.scalars(stmt).all()

    return posts


@app.get("/forum/post/reply", status_code=status.HTTP_200_OK)
def get_forum_post_replies(post_id: int, db: Session = Depends(get_db)):
    # First get immediate replies
    stmt = (
        select(models.PostReply)
        .where(models.PostReply.post_id == post_id)
    )
    replies = db.scalars(stmt).all()

    return replies
