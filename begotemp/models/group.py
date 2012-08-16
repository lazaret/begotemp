# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for geographical groups."""
#from sqlalchemy import *
#from sqlalchemy.orm import *
#from geoalchemy import *


from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from anuket.models import Base


class Group(Base):
    """ Table for the geographical groups - POLYGONS - Lambert93."""
    __tablename__ = 'group'
    group_id = Column(Integer, primary_key=True)
    group_number = Column(Integer, nullable=False)
    zone_id = Column(Integer, ForeignKey('zone.zone_id'))

    # One-to-many relationship between groups and rocks
    group_rocks = relationship('Rock', backref='group')

#    def __init__(self, zone, group):
#        self.group_number = group
#        self.zone_id = zone
