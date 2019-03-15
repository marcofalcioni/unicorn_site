import site
from logging import getLogger, basicConfig
from pyramid.config import Configurator


_LOGGER = getLogger(__name__)

_LOGGER.warn("got here")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()

