# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for geographical zones."""
from geoalchemy import GeometryColumn, GeometryDDL, Polygon, Point
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from anuket.models import Base


class Zone(Base):
    """ Table for the geographical zones - POLYGONS - Lambert93."""
    __tablename__ = 'zone'

    zone_id = Column(Integer, primary_key=True)
    zone_number = Column(Integer, nullable=False)
    geo_polygon = GeometryColumn(Polygon(2, srid=2154, spatial_index=False))
    geo_centroid = GeometryColumn(Point(2, srid=2154, spatial_index=False))

    # One-to-many relationship between zones and groups
    zone_groups = relationship('Group', backref='zone')

#    # One-to-many relationship between zones and rocks
#    zone_rocks = relationship(
#        'Rock', primaryjoin=
#        "and_(Zone.zone_id==Group.zone_id, Group.group_id==Rock.group_id)",
#        foreign_keys="[Group.zone_id, Rock.group_id]",
#        viewonly=True, remote_side="[Group.group_id]")
#    #TODO test the above and evaluate if it's neccessary
#    #TODO add backref in the rocks ?

#    @classmethod
#    def count_groups(zone_id=None):
#        """ Count the children groups."""
#        if zone_id:
#            from anuket.models import DBSession
#            from begotemp.models.group import Group
#            query = DBSession.query(Group).filter(Group.zone_id==zone_id).count()
#            #TODO tests if the above work
#            #test = self.zone_rocks.count(zone_id)
#            return query

#    @classmethod
#    def count_rocks(zone_id=None, ):
#        """ Count the grand children rocks."""
#        if zone_id:
#            from anuket.models import DBSession
#            from begotemp.models.rocks import Group, Rocks
#            query = DBSession.query(Rocks).join(Group).filter(Rock.).count()
#            #TODO tests if the above work
#            #test = self.zone_rocks.count(zone_id)
#            return query


#TODO: decide if we use @classmethod or @hybrid_property



#    def __init__(self, zone):
#        self.zone_number = zone
#
#    def set_centroid(self, poly):
#        """Define the centroid geometry from the polygon geometry"""
#        self.geo_centroid = Centroid(poly)

GeometryDDL(Zone.__table__)

#TODOs
# review set_centroid/geo_centroid: in classmethod ? in field ?
# avaivalble directly from geoalchemy.functions ?
# add index to zone_number ? No need, too less records expected
# review __init__
# add __repr__
# Add a Secteurs model ?
# rename Zone and Group to GeoZone and GeoGroups (class and table) ?
# or something like PolygonZone PolygonGroup ?
#TODO zone_number must be unique
#TODO setup backref intependently to minimize database load see
#http://pieces.openpolitics.com/2006/07/sqlalchemy-beware-of-backref/
