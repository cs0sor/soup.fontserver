from webob import Request
from webob import Response
from soupfontserver.routes import Router

class ServerFactory(object):
    
    def __init__(self, global_config):
        self.global_config = global_config
        

    def __call__(self, environ, start_response):
        self.request = Request(environ)
        router = Router(self.request, self.global_config)
        
        res = router()
        return res(environ, start_response)
        