# -*- coding: utf-8 -*-

# attempt to use WTForms instead of simpleforms
# for edition rocks

from wtforms import Form, TextField, validators


class RockForm(Form):
    rock_number = TextField(u'Number', validators=[
        validators.Length(max=10),
        validators.required()])

