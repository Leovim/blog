#coding=utf8

import hashlib
from datetime import datetime

from sqlalchemy import Column, Integer, String

from blog.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r %r>' % (self.name, self.email)


class User(Base):
    __tablename__ = 'user'
    user_ID = Column(Integer, primary_key=True)
    name = Column(String(16), unique=True)
    email = Column(String(40), unique=True)
    passwd = Column(String(32))

    def __init__(self, name=None, email=None, passwd=None):
        self.name = name
        self.email = email
        m = hashlib.md5(passwd)
        self.passwd = m.hexdigest()

    def __repr__(self):
        return '<User %r %r %r>' % (self.user_ID, self.name, self.email)


class Category(Base):
    """ table category """
    __tablename__ = 'category'
    category_ID = Column(Integer, primary_key=True)
    category_name = Column(String(45), unique=True)
    category_num = Column(Integer)

    def __init__(self, name=None):
        self.category_name = name
        
    def __repr__(self):
        return '<Category %r %r>' % (self.category_name,
                                     self.category_num)


class Tag(Base):
    """ table tag """
    __tablename__ = 'tag'
    tag_ID = Column(Integer, primary_key=True)
    tag_num = Column(Integer)

    def __init__(self, name=None):
        self.tag_name = name
        
    def __repr__(self):
        return '<Tag %r %r>' % (self.tag_name, self.tag_num)


class Article(Base):
    """ table article"""
    article_ID = Column(Integer, primary_key=True)
    article_title = Column(String(60))
    article_author = Column(Integer, ForeignKey('user.user_ID'))

    def __init__(self, title=None, time_published=datetime.now(), 
                 content=None, tags=None):
