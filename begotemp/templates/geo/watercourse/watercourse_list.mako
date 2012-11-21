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
      <th>${_(u"Watercourse")}</th>
      <th>${_(u"Linestring")}</th>
    </tr>
  </thead>
##  <tfoot>
##  </tfoot>
  <tbody>
    % for watercourse in watercourses:
    <tr>
      <td> <!-- tool button -->
        <div class="btn-group">
          <button data-toggle="dropdown" class="btn btn-mini dropdown-toggle"><span class="icon">`</span> <span class="caret"/></button>
          <ul class="dropdown-menu">
##            <li><a href="${request.route_path("geo.watercourse_show", watercourse_id=watercourse.watercourse_id)}"><span class="icon">z</span>${_(u"Show")}</a></li>
##            <li><a href="${request.route_path("geo.watercourse_edit", watercourse_id=watercourse.watercourse_id)}"><span class="icon">></span>${_(u"Edit")}</a></li>
##            <li><a href="#confirm_delete" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("geo.watercourse_delete", watercourse_id=watercourse.watercourse_id)}');"><span class="icon">Ë</span>${_(u"Delete")}</a></li>
          </ul>
        </div>
      </td>
      <td><strong>${watercourse.watercourse_name}</strong></td>
      %if watercourse.geo_linestring:
        <td><span class="icon">Ã</span></td>
      %else:
        <td><span class="icon">Â</span></td>
      %endif
    </tr>
    % endfor
  </tbody>
</table>


## Pager
${pager(watercourses)}

#### Confirm delete modal
##${confirm_delete()}

## Page title
<%block name="page_title">
${_(u"Watercourse list")}
</%block>

## Add record button
<%block name="add_button">
<a href="${request.route_path("geo.watercourse_add")}" class="btn btn-primary pull-right"><span class="icon">@</span>${_(u"Add new watercourse")}</a>
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
