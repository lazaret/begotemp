# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for the lakes."""
from geoalchemy import GeometryColumn, GeometryDDL, Polygon, Point
from sqlalchemy import Column, Unicode, Integer

from anuket.models import Base


class Lake(Base):
    """ Table for the lakes - POLYGONS - Lambert93."""
    __tablename__ = 'lake'

    lake_id = Column(Integer, primary_key=True)
    lake_name = Column(Unicode)
    geo_polygon = GeometryColumn(Polygon(2, srid=2154, spatial_index=False))
    geo_centroid = GeometryColumn(Point(2, srid=2154, spatial_index=False))


GeometryDDL(Lake.__table__)
