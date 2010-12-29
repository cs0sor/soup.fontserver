from soupfontserver.static import StaticDir
from paste.urlparser import StaticURLParser
from webob import Request
class ServerFactory(object):
    
    def __init__(self, global_config):
        self.global_config = global_config
        

    def __call__(self, request, handler):
        self.request = Request(request)
        self.static = StaticDir(self.global_config, self.request)
        self.handler = handler
        static = self.static()
        