from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings

from sqlalchemy import engine_from_config

import anuket
from anuket.models import DBSession
from anuket.models.rootfactory import RootFactory
from anuket.security import get_auth_user


from begotemp.models.zone import Zone
from begotemp.models.group import Group
from begotemp.models.rock import Rock
from begotemp.models.figure import Figure


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # configure SQLAlchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    # configure the root factory (used for Auth & Auth)
    root_factory = RootFactory
    config.set_root_factory(root_factory)
    # configure session
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    # configure auth & auth
    config.include(anuket.add_authorization)
    # set an auth_user object
    config.set_request_property(get_auth_user, 'auth_user', reify=True)

    # configure subscribers
##    config.include(anuket.subscribers)
##Comented to avoid crsf check
##TODO bring back CSRF
    from pyramid.events import BeforeRender, NewRequest
    config.add_subscriber(anuket.subscribers.add_renderer_globals, BeforeRender)
    config.add_subscriber(anuket.subscribers.add_localizer, NewRequest)


    # configure static views
    config.include(anuket.add_static_views)
    # configure routes
    config.include(anuket.views.root)
    config.include(anuket.views.tools)
    config.include(anuket.views.user)

#TODO improve this
    from begotemp.views import geo_zone, geo_group, geo_rock
    config.include(geo_zone)
    config.include(geo_group)
    config.include(geo_rock)
    ## configure views
    config.scan('anuket')
    config.scan()



    config.add_translation_dirs('anuket:locale')
    config.set_locale_negotiator('anuket.lib.i18n.locale_negotiator')

    return config.make_wsgi_app()
