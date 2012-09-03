## -*- coding:utf-8 -*-
##
<%inherit file="begotemp:templates/rock/base.mako" />
###<%namespace file="user_form_fields.mako" import="user_form_fields"/>
###<%namespace file="password_form_fields.mako" import="password_form_fields"/>

<div class="row">
  <div class="span7 offset1">
    <form action="" method="post" class="form-horizontal">

      <fieldset>
      <legend></legend>
        <div class="${'control-group error' if form.rock_number.errors else 'control-group'}">
        <label for="rock_number" class="control-label">
          ${form.rock_number.label}
        </label>
        <div class="controls">
          ${form.rock_number()}
          %if form.rock_number:
            %for error in form.rock_number.errors:
              <span class="help-inline"><span class="icon">8</span>${error}</span>
            %endfor
          %else:
            ✩
          %endif
        </div>
      </div>

      <div class="control-group">
        <label for="group" class="control-label">
          ${form.group.label}
        </label>
        <div class="controls">
          ${form.group()}
        </div>
      </div>
      </fieldset>

      <fieldset>
      <legend>Position</legend>

      <div class="${'control-group error' if form.point_x.errors else 'control-group'}">
        <label for="point_x" class="control-label">
          ${form.point_x.label}
        </label>
        <div class="controls">
          ${form.point_x()}
          %if form.point_y.errors:
            %for error in form.point_x.errors:
              <span class="help-inline"><span class="icon">8</span>${error}</span>
            %endfor
          %else:
            ✩
          %endif
        </div>
      </div>

      <div class="${'control-group error' if form.point_y.errors else 'control-group'}">
        <label for="point_y" class="control-label">
          ${form.point_y.label}
        </label>
        <div class="controls">
          ${form.point_y()}
          %if form.point_y.errors:
            %for error in form.point_y.errors:
              <span class="help-inline"><span class="icon">8</span>${error}</span>
            %endfor
          %else:
            ✩
          %endif
        </div>
      </div>

      <div class="${'control-group error' if form.point_z.errors else 'control-group'}">
        <label for="point_z" class="control-label">
          ${form.point_z.label}
        </label>
        <div class="controls">
          ${form.point_z()}
          %if form.point_z.errors:
            %for error in form.point_y.errors:
              <span class="help-inline"><span class="icon">8</span>${error}</span>
            %endfor
          %endif
        </div>
      </div>
      </fieldset>

      <fieldset>
      <legend></legend>
      <div class="control-group">
        <label for="year" class="control-label">
          ${form.year.label}
        </label>
        <div class="controls">
          ${form.year()}
        </div>
      </div>
      </fieldset>

      <div class="form-actions">
        <div class="row">
          <div class="span2">
            <button type="submit" name="form_submitted" class="btn btn-primary"><span class="icon">Ã</span>${_(u"Submit")}</button>
          </div>
          <div class="span2">
            <button type="button" onclick="window.location='/rock'" class="btn"><span class="icon">Â</span>${_(u"Cancel")}</button>
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
${_(u"Add rock")}
</%def>
