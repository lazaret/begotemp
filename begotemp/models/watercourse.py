# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for the watercourses."""
from geoalchemy import GeometryColumn, GeometryDDL, LineString
from sqlalchemy import Column, Unicode, Integer

from anuket.models import Base


class Watercourse(Base):
    """ Table for the watercourses - LINESTRINGS - Lambert93."""
    __tablename__ = 'watercourse'

    watercourse_id = Column(Integer, primary_key=True)
    watercourse_name = Column(Unicode, unique=True)
    geo_linestring = GeometryColumn(LineString(2, srid=2154, spatial_index=False))


GeometryDDL(Watercourse.__table__)
