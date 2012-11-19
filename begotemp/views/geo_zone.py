# -*- coding: utf-8 -*-
""" Tools for geographical zones management."""
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from webhelpers import paginate

from anuket.models import DBSession
from begotemp.models.zone import Zone
from begotemp.models.group import Group
from begotemp.models.rock import Rock
from begotemp.forms import ZoneForm


log = logging.getLogger(__name__)


def includeme(config):

    config.add_route('geo.zone_list', '/geo/zone')
    config.add_route('geo.zone_add', '/geo/zone/add')


def get_zone_stats():
    """ Get basic database statistics.

    :return: zones and groups counts from the database
    :rtype: dictionary
    """
    zonecount = DBSession.query(Zone.zone_id).count()
    groupcount = DBSession.query(Group.group_id).count()
    rockcount = DBSession.query(Rock.rock_id).count()
    engravingcount = None
    return dict(zonecount=zonecount, groupcount=groupcount,
                rockcount=rockcount, engravingcount=engravingcount)


@view_config(route_name='geo.zone_list', permission='admin',
             renderer='/geo/zone/zone_list.mako')
def zone_list_view(request):

    _ = request.translate
    stats = get_zone_stats()
    # construct the query
    zones = DBSession.query(Zone)
    zones = zones.order_by(Zone.zone_number)
    # add a flash message for empty results
    if zones.count() == 0:
        request.session.flash(_(u"There is no results!"), 'error')
    # paginate results
    page_url = paginate.PageURL_WebOb(request)
    zones = paginate.Page(zones,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)
    return dict(zones=zones, stats=stats)


@view_config(route_name='geo.zone_add', permission='admin',
             renderer='/geo/zone/zone_add.mako')
def zone_add_view(request):

    _ = request.translate
    form = ZoneForm(request.POST)
    if 'form_submitted' in request.params and form.validate():
        zone = Zone()
        form.populate_obj(zone)
        DBSession.add(zone)
        request.session.flash(_(u"Zone added."), 'success')
        return HTTPFound(location=request.route_path('geo.zone_list'))
    return dict(form=form)
