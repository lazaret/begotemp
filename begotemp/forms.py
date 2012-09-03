# -*"- coding: utf-8 -*-

# attempt to use WTForms instead of simpleforms
# for edition rocks

from wtforms import Form, FloatField, IntegerField, TextField, validators
from  wtforms.ext.sqlalchemy.fields import QuerySelectField

from anuket.models import DBSession
from begotemp.models.group import Group
from begotemp.models.zone import Zone



class ZoneForm(Form):
    zone_number = IntegerField(u'Zone number', validators=[
        validators.required()])


def get_zones():
    return DBSession.query(Zone).order_by(Zone.zone_number).all()
#TODO move in models ?

class GroupForm(Form):
    group_number = IntegerField(u'Group number', validators=[
        validators.required()])

    zones = QuerySelectField(u'Zone', get_label='zone_number',
        query_factory=get_zones)


def get_groups():
    return DBSession.query(Group).order_by(Group.group_number).all()

class RockForm(Form):
    rock_number = TextField(u'Rock number', validators=[
        validators.Length(max=10),
        validators.required()])

    #TODO change 'group' to 'groups'
    group = QuerySelectField(query_factory=get_groups)

    point_x = FloatField(u'X', validators=[
        validators.required()])
    point_y = FloatField(u'Y', validators=[
        validators.required()])
    point_z = FloatField(u'Z')

    year = IntegerField(u'Year')



