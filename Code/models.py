from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region = Column(String)
    nights = Column(Integer)
    days = relationship("Day", back_populates="itinerary", cascade="all, delete")

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'))
    day_number = Column(Integer)
    itinerary = relationship("Itinerary", back_populates="days")
    activities = relationship("Activity", back_populates="day", cascade="all, delete")
    transfers = relationship("Transfer", back_populates="day", cascade="all, delete")
    accommodations = relationship("Accommodation", back_populates="day", cascade="all, delete")

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Day", back_populates="activities")

class Transfer(Base):
    __tablename__ = 'transfers'
    id = Column(Integer, primary_key=True)
    from_location = Column(String)
    to_location = Column(String)
    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Day", back_populates="transfers")

class Accommodation(Base):
    __tablename__ = 'accommodations'
    id = Column(Integer, primary_key=True)
    hotel_name = Column(String)
    address = Column(Text)
    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Day", back_populates="accommodations")
