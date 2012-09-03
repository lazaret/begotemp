# -*- coding: utf-8 -*-

import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from webhelpers import paginate

from anuket.models import DBSession
from begotemp.models.rock import Rock
from begotemp.forms import RockForm


log = logging.getLogger(__name__)


def includeme(config):

    config.add_route('rock_list', '/rock')
    config.add_route('rock_add', '/rock/add')


@view_config(route_name='rock_list', permission='admin',
             renderer='/rock/rock_list.mako')
def rock_list_view(request):

    _ = request.translate
    stats=None
    sortable_columns = ['rock_number']
    column = request.params.get('sort')
    # construct the query
    rocks = DBSession.query(Rock)
    if column and column in sortable_columns:
        rocks = rocks.order_by(column)
    else:
        rocks = rocks.order_by(Rock.rock_number)
    # add a flash message for empty results
    if rocks.count() == 0:
        request.session.flash(_(u"There is no results!"), 'error')

    # paginate results
    page_url = paginate.PageURL_WebOb(request)
    rocks = paginate.Page(rocks,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)
    return dict(rocks=rocks, stats=stats)


@view_config(route_name='rock_add', permission='admin',
             renderer='/rock/rock_add.mako')
def rock_add_view(request):

    _ = request.translate
    form = RockForm(request.POST)
    if 'form_submitted' in request.params and form.validate():
        rock = Rock()
        form.populate_obj(rock)
        DBSession.add(rock)
        request.session.flash(_(u"Rock added."), 'success')
        return HTTPFound(location=request.route_path('rock_list'))

    return dict(form=form)

#TODO add two related dropdown, first zone and after group


#TODO change 'rock' to 'geo_rock' 'geo/rock' ?
