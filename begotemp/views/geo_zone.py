# -*- coding: utf-8 -*-
""" Tools for geographical zones management."""
import logging
from pyramid.view import view_config
from webhelpers import paginate


from anuket.models import DBSession
from begotemp.models.zone import Zone


log = logging.getLogger(__name__)


def includeme(config):

    config.add_route('geo.zone_list', '/geo/zone')


@view_config(route_name='geo.zone_list', permission='admin',
             renderer='/geo/zone/zone_list.mako')
def zone_list_view(request):

    stats=None

    # construct the query
    zones = DBSession.query(Zone)
    zones = zones.order_by(Zone.zone_number)

    # paginate results
    page_url = paginate.PageURL_WebOb(request)
    zones = paginate.Page(zones,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)


    return dict(zones=zones, stats=stats)