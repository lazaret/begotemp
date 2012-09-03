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
# add index to zone_number ?
# review __init__
# add __repr__
# Add a Secteurs model ?
# rename Zone and Group to GeoZone and GeoGroups (class and table) ?
# or something like PolygonZone PolygonGroup ?
#TODO zone_number must be unique
#TODO setup backref intependently to minimize database load see
#http://pieces.openpolitics.com/2006/07/sqlalchemy-beware-of-backref/
