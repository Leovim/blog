#coding=utf8
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from blog import app
from data import (db, Category, Tag, Article, Comment, User,\
        Link, BlackList, Subscriber)
