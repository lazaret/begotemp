# -*- coding: utf-8 -*-
""" Tools for geographical zones management."""
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from webhelpers import paginate

from anuket.models import DBSession
from begotemp.models.group import Group
from begotemp.forms import GroupForm


log = logging.getLogger(__name__)


def includeme(config):

    config.add_route('geo.group_list', '/geo/group')
    config.add_route('geo.group_add', '/geo/group/add')


@view_config(route_name='geo.group_list', permission='admin',
             renderer='/geo/group/group_list.mako')
def group_list_view(request):

    _ = request.translate
    stats=None
    sortable_columns = ['group_number', 'zone_number']
    #TODO correct zone_number sorting and listing
    column = request.params.get('sort')
    # construct the query
    groups = DBSession.query(Group)
    if column and column in sortable_columns:
        groups = groups.order_by(column)
    else:
        groups = groups.order_by(Group.group_number)
    # add a flash message for empty results
    if groups.count() == 0:
        request.session.flash(_(u"There is no results!"), 'error')

    # paginate results
    page_url = paginate.PageURL_WebOb(request)
    groups = paginate.Page(groups,
                           page=int(request.params.get("page", 1)),
                           items_per_page=20,
                           url=page_url)
    return dict(groups=groups, stats=stats)


@view_config(route_name='geo.group_add', permission='admin',
             renderer='/geo/group/group_add.mako')
def zone_add_view(request):

    _ = request.translate
    form = GroupForm(request.POST)
    if 'form_submitted' in request.params and form.validate():
        group = Group()
        form.populate_obj(group)
        DBSession.add(group)
        request.session.flash(_(u"Group added."), 'success')
        return HTTPFound(location=request.route_path('geo.group_list'))

    return dict(form=form)
