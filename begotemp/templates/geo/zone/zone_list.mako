## -*- coding:utf-8 -*-
##
<%inherit file="begotemp:templates/geo/base.mako" />
##<%namespace file="anuket:templates/widgets/confirm_delete.mako" import="confirm_delete"/>
<%namespace file="anuket:templates/widgets/pager.mako" import="pager"/>


<table class="table table-striped table-condensed table-bordered">
  <thead>
## TODO tests two line thead
##    <tr>
##      <th rowspan="2" style="width: 50px;"></th>
##      <th colspan="2">${_(u"Datas")}</th>
##      <th></th>
##      <th colspan="3">${_(u"Statistics")}</th>
##    </tr>
    <tr>
      <th style="width: 50px;"></th>
      <th>${_(u"Zone")}</th>
      <th>${_(u"Polygon")}</th>
      <th>${_(u"Groups")}</th>
      <th>${_(u"Rocks")}</th>
      <th>${_(u"Engravings")}</th>
    </tr>
  </thead>
##  <tfoot>
##  </tfoot>
  <tbody>
    % for zone in zones:
    <tr>
      <td> <!-- tool button -->
        <div class="btn-group">
          <button data-toggle="dropdown" class="btn btn-mini dropdown-toggle"><span class="icon">`</span> <span class="caret"/></button>
          <ul class="dropdown-menu">
##            <li><a href="${request.route_path("geo.zone_show", zone_id=zone.zone_id)}"><span class="icon">z</span>${_(u"Show")}</a></li>
##            <li><a href="${request.route_path("geo.zone_edit", zone_id=zone.zone_id)}"><span class="icon">></span>${_(u"Edit")}</a></li>
##            <li><a href="#confirm_delete" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("geo.zone_delete", zone_id=zone.zone_id)}');"><span class="icon">Ë</span>${_(u"Delete")}</a></li>
          </ul>
        </div>
      </td>
      <td><strong>${zone.zone_number}</strong></td>
      %if zone.geo_polygon:
        <td><span class="icon">Ã</span></td>
      %else:
        <td><span class="icon">Â</span></td>
      %endif
      <td>${zone.groups_count}</td>
      <td>${zone.rocks_count}</td>
      <td></td>
    </tr>
    % endfor
  </tbody>
</table>


## Pager
${pager(zones)}

#### Confirm delete modal
##${confirm_delete()}

## Page title
<%block name="page_title">
${_(u"Zone list")}
</%block>

## Add record button
<%block name="add_button">
<a href="${request.route_path("geo.zone_add")}" class="btn btn-primary pull-right"><span class="icon">@</span>${_(u"Add new zone")}</a>
</%block>

#### Aside search box
##<%block name="aside_search">
##  <% search = request.params.get('search') %>
##  %if search:
##    <% placeholder = search %>
##  %else:
##    <% placeholder = _(u"Search") %>
##  %endif
##<form action="${request.route_path('tools.user_list')}" class="well form-search">
##  <input type="search" name="search" placeholder="${placeholder}" class="input-small search-query">
##<button type="submit" class="btn btn-small pull-right"><span class="icon">z</span>${_(u"Search")}</button>
##</form>
##</%block>

## Aside stats table
<%block name="aside_stats">
<table class="table table-condensed table-bordered">
  <thead>
   <tr><th>${_(u"Statistics")}</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>${_("Zones")}</td>
      <td>${stats['zonecount']}</td>
    </tr>
    <tr>
      <td>${_("Groups")}</td>
      <td>${stats['groupcount']}</td>
    </tr>
    <tr>
      <td>${_("Rocks")}</td>
      <td>${stats['rockcount']}</td>
    </tr>
    <tr>
      <td>${_("Engravings")}</td>
      <td>${stats['engravingcount']}</td>
    </tr>
  </tbody>
</table>
</%block>