from soupfontserver.static import StaticDir

class Router(object):
    def __init__(self, request, global_config):
        self.request = request
        self.global_config = global_config
    
    def __call__(self):
        path = self.request.path_info.split('/')
        if path[1] == 'static':
            static = StaticDir(self.request, self.global_config)
        res = static()

        return res