from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class Comment(db.Model):
    text = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    user = db.TextProperty(required = True)

def recentComments(update = False):
    """
    Returns the recent comments form the memcache
    If update is required, adds the comment and then returns the new set of comments"""
    key = 'recent'
    comments = memcache.get(key)
    if comments is None or update:
        logging.error("DB query")
        comments = db.GqlQuery("SELECT * FROM Comment ORDER BY created DESC LIMIT 10")
        comments = list(comments)
        memcache.set(key, comments)
    return comments