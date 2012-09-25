## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/base.mako" />

${next.body()}

## Aside Menu
##<%block name="aside_menu()">
##<div style="padding: 8px 0pt;" class="well">
##  <ul class="nav nav-list">
##    <li class="nav-header">${_(u"Tools")}</li>
##    <li><a href="${request.route_path('tools.index')}"><span class="icon">a</span>${_(u"Tool list")}</a></li>
##    <li class="active"><a href="${request.route_path('tools.user_list')}"><span class="icon">L</span>${_(u"User management")}</a></li>
##  </ul>
##</div>
##</%block>


#### Top navbar links
##<%def name="top_navbar_links()">
##<ul class="nav">toto
##  <li><a href="${request.route_path('home')}"><span class="icon">S</span><b>${_(u"Home")}</b></a></li>
##</ul>
##</%def>
