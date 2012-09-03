## -*- coding:utf-8 -*-
##
<%inherit file="begotemp:templates/geo/base.mako" />
###<%namespace file="user_form_fields.mako" import="user_form_fields"/>
###<%namespace file="password_form_fields.mako" import="password_form_fields"/>

<div class="row">
  <div class="span7 offset1">
    <form action="" method="post" class="form-horizontal">

      <fieldset>
      <legend></legend>
        <div class="${'control-group error' if form.zone_number.errors else 'control-group'}">
        <label for="zone_number" class="control-label">
          ${form.zone_number.label}
        </label>
        <div class="controls">
          ${form.zone_number()}
          %if form.zone_number:
            %for error in form.zone_number.errors:
              <span class="help-inline"><span class="icon">8</span>${error}</span>
            %endfor
          %else:
            ✩
          %endif
        </div>
      </div>
      </fieldset>

      <div class="form-actions">
        <div class="row">
          <div class="span2">
            <button type="submit" name="form_submitted" class="btn btn-primary"><span class="icon">Ã</span>${_(u"Submit")}</button>
          </div>
          <div class="span2">
            <button type="button" onclick="window.location='/geo/zone'" class="btn"><span class="icon">Â</span>${_(u"Cancel")}</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>


###<div class="row">
###  <div class="span7 offset1">
###    <form action="" method="post" class="form-horizontal">
###      ${renderer.csrf_token()}
###      ${user_form_fields()}
###      ${password_form_fields()}
###      <div class="form-actions">
###        <div class="row">
###          <div class="span2">
###            <button type="submit" name="form_submitted" class="btn btn-primary"><span class="icon">Ã</span>${_(u"Submit")}</button>
###          </div>
###          <div class="span2">
###            <button type="button" onclick="window.location='/tools/user'" class="btn"><span class="icon">Â</span>${_(u"Cancel")}</button>
###          </div>
###        </div>
###      </div>
###    </form>
###  </div>
###</div>

## Page title
<%def name="page_title()">
${_(u"Add zone")}
</%def>
