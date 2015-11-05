from mainHandler import *
from commentsdb import *
from time import sleep

class home(mainHandler):
    """
    Handler class for home
    """
    def get(self, **kwargs):
        user = users.get_current_user()
        if user:
            username = user.nickname()
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = users.create_logout_url(self.request.uri)
        else:
            username = None
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = "/"
        comments_ = recentComments()
        self.renderPage("version0.html", username = username, loginLink = loginLink, logoutLink = logoutLink, comments = comments_)

    def post(self, **kwargs):
        name = self.request.get('dname')
        text = self.request.get('comment')
        if name and text:
            c = Comment(text = text, user = name)
            c.put()
            sleep(0.1)
            recentComments(True)
        self.redirect('/')
class cacheFlush(mainHandler):
    """
    Flushes the cache
    """
    def get(self):
        memcache.flush_all()
        self.redirect("/")