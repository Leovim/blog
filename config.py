#coding=utf-8

DEBUG = True
FRAGMENT_PER_PAGE = 10

# -- Flask SQLALCHEMY --
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'leo'
MYSQL_PASS = 'wahrr7231657'
MYSQL_DB = 'blog'

# mysql://leo:wahrr7231657@localhost:3306/blog
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS,
                                                      MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
