import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    namename = Column(String(250), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    Favorites_Planets = relationship("Favorites_Planets", uselist=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    person_name = Column(String)
    favorite_people = relationship("Favorites_People", uselist=False)

class Favorites_Planets(Base):
    __tablename__ = 'favorite_planets'
    fav_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship("Users", backref="favorite_planets")
    planet = relationship("Planets", uselist=False)

class Favorites_People(Base):
    __tablename__ = 'favorite_people'
    fav_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    person_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("Users", backref="favorite_people")
    person = relationship("People", uselist=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
