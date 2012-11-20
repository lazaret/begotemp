## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/base.mako" />

${next.body()}

## Aside Menu
##<%block name="aside_menu">
##<div style="padding: 8px 0pt;" class="well">
##  <ul class="nav nav-list">
##    <li class="nav-header">${_(u"Tools")}</li>
##    <li><a href="${request.route_path('tools.index')}"><span class="icon">a</span>${_(u"Tool list")}</a></li>
##    <li class="active"><a href="${request.route_path('tools.user_list')}"><span class="icon">L</span>${_(u"User management")}</a></li>
##  </ul>
##</div>
##</%block>


#### Left navbar links
<%block name="left_navbar_links">
<li class="dropdown">
  <a href="#" data-toggle="dropdown" class="dropdown-toggle"><span class="icon">6</span><b>${_(u"Geography")}</b><b class="caret"/></b></a>
  <ul class="dropdown-menu">
    <li><a href="${request.route_path('geo.zone_list')}">${_("Zone")}</a></li>
    <li><a href="${request.route_path('geo.group_list')}">${_("Group")}</a></li>
    <li><a href="${request.route_path('geo.rock_list')}">${_("Rock")}</a></li>
  </ul>
</li>
</%block>
