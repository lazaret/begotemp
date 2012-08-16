# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for geographical zones."""
#from sqlalchemy import *
#from sqlalchemy.orm import *
#from geoalchemy import *
#
#from petroglyphsmap.model.meta import Base
#

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from anuket.models import Base


class Zone(Base):
    """ Table for the geographical zones - POLYGONS - Lambert93."""
    __tablename__ = 'zone'
    zone_id = Column(Integer, primary_key=True)
    zone_number = Column(Integer, nullable=False)
#    geo_polygon = GeometryColumn(Polygon(2, srid=2154, spatial_index=False))
#    geo_centroid = GeometryColumn(Point(2, srid=2154, spatial_index=False))

    # One-to-many relationship between zones and groups
    zone_groups = relationship('Group', backref='zone')

#
#    def __init__(self, zone):
#        self.zone_number = zone
#
#    def set_centroid(self, poly):
#        """Define the centroid geometry from the polygon geometry"""
#        self.geo_centroid = Centroid(poly)
