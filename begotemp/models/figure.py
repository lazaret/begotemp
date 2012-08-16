# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for figures."""
#from sqlalchemy import *
#from sqlalchemy.orm import *
#from geoalchemy import *

from sqlalchemy import Column, ForeignKey, Integer, Unicode

from anuket.models import Base


class Figure(Base):
    """ Table for the figures."""
    __tablename__ = 'figure'
    figure_id = Column(Integer, primary_key=True)
    figure_number = Column(Unicode(15), nullable=False)
    rock_id = Column(Integer, ForeignKey('rock.rock_id'))

#    identity = Column(Unicode(30), index=True)                                # Index to improve the queries
#    alternative_identity = Column(Unicode(30), index=True)                    # Index to improve the queries
#    face = Column(Unicode(1))
#
#    def __init__(self, zone, group, rock, figure, identity, alt_identity, face):
#        self.figure_number = figure
#        self.identity = identity
#        self.alternative_identity = alt_identity
#        self.rock_id = rockid_from_zgr(zone, group, rock)
#        self.face = face
#