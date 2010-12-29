import soupfontserver
from soupfontserver.server import ServerFactory
     
def app(global_config, **kw):

    sf = ServerFactory(global_config)
    return sf
    