from soupfontserver.static import StaticDir
from paste.urlparser import StaticURLParser
from webob import Request
from webob import Response

class ServerFactory(object):
    
    def __init__(self, global_config):
        self.global_config = global_config
        

    def __call__(self, environ, start_response):
        self.request = Request(environ)
        self.static = StaticDir(self.request, self.global_config)
        res = self.static()
        return res(environ, start_response)
        