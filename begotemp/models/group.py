# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for geographical groups."""
from geoalchemy import GeometryColumn, GeometryDDL, Polygon, Point
from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from anuket.models import Base


class Group(Base):
    """ Table for the geographical groups - POLYGONS - Lambert93."""
    __tablename__ = 'group'
    __table_args__ = (UniqueConstraint('group_number', 'zone_id'),)

    group_id = Column(Integer, primary_key=True)
    group_number = Column(Integer, nullable=False)
    geo_polygon = GeometryColumn(Polygon(2, srid=2154, spatial_index=False))
    geo_centroid = GeometryColumn(Point(2, srid=2154, spatial_index=False))

    # One-to-many relationship between zones and groups
    zone_id = Column(Integer, ForeignKey('zone.zone_id'))
    # One-to-many relationship between groups and rocks
    group_rocks = relationship('Rock', backref='group')

#    def __init__(self, zone, group):
#        self.group_number = group
#        self.zone_id = zone


GeometryDDL(Group.__table__)


#TODOs
# add index to group_number ?
# review __init__
# add __repr__
# find another name for group_id to avoi confusion with AuthGroup.group_id ?
# rename Zone and groups to GeoZone and GeoGroup (class and table) ?
# or something like PolygonZone PolygonGroup ?
# the geographical polygon seems to not be defined
#
# we must change the table name as 'group' is a SQL reserved word
