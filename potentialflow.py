import webapp2
from result import result
from home import home
from home import cacheFlush

app = webapp2.WSGIApplication([('/', home),
                               ('/result', result),
                               ('/flush', cacheFlush)],
                              debug = True)