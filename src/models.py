import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)                      #declaro esta como mi clave primaria
    username = Column(String(250), nullable=False)              #declaro la columna username
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    DateSuscription = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    Password = Column(String(250), nullable=False)
    def to_dict(self):                                          #defino el dictionary de mi clase para que le asigne las propiedades al objeto
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname" : self.lastname,
            "Date_suscription" : self.DateSuscription,
            "email" : self.email,
            "password" : self.password
        }

class Planetas(Base):
    #estoy creando una PLANETAS media que hereda el ID de mi tabla Post
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)                                        #este tipo de dato me permite escoger en tre imagen video o galeria
    url = Column(String(250))
                                                    #estoy relacionando la variable post  de la clase Post en mi clase Media.
    
    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
        }

class Personas(Base):
    #estoy creando una tabla PERSONAS que hereda el ID de mi tabla Post
    __tablename__ = 'personas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)                                        #este tipo de dato me permite escoger entre imagen/video/galeria
    url = Column(String(250))

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
        }

class Especies(Base):
    #estoy creando una tabla ESPECIES que hereda el ID de mi tabla Post
    __tablename__ = 'especies'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)                                        #este tipo de dato me permite escoger en tre imagen video o galeria
    url = Column(String(250))    
    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
        }

class Favorites(Base):
    #estoy creando una clase FAVORITOS que hereda el ID de mi tabla User y el ID de mi tabla Comment
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))                            #estoy indicando que mi clave post id se relaciona con la clave id de post
    planetas = relationship(Planetas)
    persona_id = Column(Integer, ForeignKey('personas.id'))                            #estoy indicando que mi clave post id se relaciona con la clave id de post
    personas = relationship(Personas)
    especie_id = Column(Integer, ForeignKey('especies.id'))                            #estoy indicando que mi clave post id se relaciona con la clave id de post
    especies = relationship(Especies)  
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta_id": self.planeta_id,
            "personas_id": self.persona_id,
            "especies_id": self.especie_id
        }




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')