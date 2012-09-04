## -*- coding:utf-8 -*-
##
<%inherit file="begotemp:templates/geo/base.mako" />
##<%namespace file="anuket:templates/widgets/confirm_delete.mako" import="confirm_delete"/>
<%namespace file="anuket:templates/widgets/pager.mako" import="pager"/>


<table class="table table-striped table-condensed table-bordered">
  <thead>
    <tr>
      <th style="width: 50px;"></th>
      <th>${sortable_link('rock_number', u"Rock")}</th>
      <th>${sortable_link('group_number', u"Group")}</th>
##      <th>${sortable_link('last_name', u"Last name")}</th>
      <th>${_(u"X")}</th>
      <th>${_(u"Y")}</th>
      <th>${_(u"Z")}</th>
      <th>${_(u"Year")}</th>
    </tr>
  </thead>
##  <tfoot>
##  </tfoot>
  <tbody>
    % for rock in rocks:
    <tr>
      <td> <!-- tool button -->
        <div class="btn-group">
          <button data-toggle="dropdown" class="btn btn-mini dropdown-toggle"><span class="icon">`</span> <span class="caret"/></button>
          <ul class="dropdown-menu">
##            <li><a href="${request.route_path("geo.rock_show", rock_id=rock.rock_id)}"><span class="icon">z</span>${_(u"Show")}</a></li>
##            <li><a href="${request.route_path("geo.rock_edit", rock_id=rock.rock_id)}"><span class="icon">></span>${_(u"Edit")}</a></li>
##            <li><a href="#confirm_delete" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("geo.rock_delete", rock_id=rock.rock_id)}');"><span class="icon">Ë</span>${_(u"Delete")}</a></li>
          </ul>
        </div>
      </td>
      <td>${rock.rock_number}</td>
      <td>${rock.group.group_number}</td>
      <td>${rock.point_x}</td>
      <td>${rock.point_y}</td>
      <td>${rock.point_z}</td>
      <td>${rock.year}</td>
    </tr>
    % endfor
  </tbody>
</table>


## Pager
${pager(rocks)}

#### Confirm delete modal
##${confirm_delete()}


## Page title
<%def name="page_title()">
${_(u"Rock list")}
</%def>

## Add record button
<%def name="add_button()">
  <a href="${request.route_path("geo.rock_add")}" class="btn btn-primary pull-right"><span class="icon">@</span>${_(u"Add new rock")}</a>
</%def>

## Sortable column link
<%def name="sortable_link(column, textlink)">
  <% search = request.params.get('search') %>
  <% sort = request.params.get('sort') %>
  <% postlink = "?sort="+column %>
  %if search:
    <% postlink = postlink+"&search="+search %>
  %endif
  %if sort==column:
    <% arrow = u" ▾" %>
  %else:
    <% arrow = None %>
  %endif
  <a href="${request.route_path('geo.rock_list')}${postlink}">${_(textlink)}${arrow}</a>
</%def>

#### Aside search box
##<%def name="aside_search()">
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
##</%def>

#### Aside stats box
##<%def name="aside_stats()">
##<table class="table table-condensed table-bordered">
##  <thead>
##   <tr><th>${_(u"Statistics")}</th></tr>
##  <thead>
##  <tbody>
##    <tr>
##      <td>${_("Users")}</td>
##      <td>${stats['usercount']}</td>
##    </tr>
##    <tr>
##      <td>${_("Groups")}</td>
##      <td>${stats['groupcount']}</td>
##    </tr>
##  </tbody>
##</table>
##</%def>
