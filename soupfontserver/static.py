import ConfigParser, os
from ConfigParser import NoSectionError, NoOptionError
from paste.urlparser import StaticURLParser

class StaticDir(object):
    def __init__(self, global_config, request):
        self.global_config = global_config
        self.request = request
        config = ConfigParser.ConfigParser()
        config_file = config.readfp(open('%s/setup.cfg' % global_config['here']))
        
        try:
            self.font_directory = config.get('font_directory', 'dir')
        
        except (NoSectionError, NoOptionError):
            print "You need to specify a [font_directory] and dir value in the setup.cfg file."
            raise
            
    def __call__(self):
        static = StaticURLParser(self.font_directory)
        import ipdb; ipdb.set_trace()
        return static
        
        
        