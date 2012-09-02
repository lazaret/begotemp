# -*- coding: utf-8 -*-

# attempt to use WTForms instead of simpleforms
# for edition rocks

from wtforms import Form, FloatField, IntegerField, TextField, validators
from  wtforms.ext.sqlalchemy.fields import QuerySelectField

from anuket.models import DBSession
from begotemp.models.group import Group


def get_groups():
    groups = DBSession.query(Group).order_by(Group.group_number).all()


class RockForm(Form):
    rock_number = TextField(u'Rock number', validators=[
        validators.Length(max=10),
        validators.required()])

    group = QuerySelectField(query_factory=get_groups)

    point_x = FloatField(u'X', validators=[
        validators.required()])
    point_y = FloatField(u'Y', validators=[
        validators.required()])
    point_z = FloatField(u'Z')

    year = IntegerField(u'Year')



