import ConfigParser, os
from ConfigParser import NoSectionError, NoOptionError
from paste.urlparser import StaticURLParser

class StaticDir(object):

    def __init__(self, request, global_config):
        self.request = request
        self.environ = self.request.environ
        config = ConfigParser.ConfigParser()
        config_file = config.readfp(open('%s/setup.cfg' % global_config['here']))
        
        try:
            self.font_directory = config.get('font_directory', 'dir')

        except (NoSectionError, NoOptionError):
            print "You need to specify a [font_directory] and dir value in the setup.cfg file."
            raise
        
        app = StaticURLParser(self.font_directory)
        self.app = app

    def __call__(self):
        self.request.blank('/')
        res = self.request.get_response(self.app)
        return res