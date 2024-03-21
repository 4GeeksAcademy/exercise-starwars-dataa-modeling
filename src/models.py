import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, nullable=False)



class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)


class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)



















## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


