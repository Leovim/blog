#conding=utf8

from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from blog import app

class nullpool_SQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

db = nullpool_SQLAlchemy(app)

class Fragment(db.Model):
    __tablename__ = 'rxs_whoop_fragment'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(20))
    content = db.Column(db.String(1024))
    pub_date = db.Column(db.DateTime)

    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.pub_date = pub_date

# -- Model For Blog --

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)

    def __unicode__(self):
        return self.name

article_tags = db.Table('tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
        db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)
