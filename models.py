from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, autoincrement=True)

    vehicle_type = relationship("VehicleType", back_populates="vehicle", uselist=False)
    coordinate = relationship("Coordinate", back_populates="vehicle", uselist=False)

    heading = Column(Float)
    sleepiness = Column(Integer)


class Coordinate(Base):
    __tablename__ = "coordinates"

    # id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    vehicle = relationship("Vehicle", back_populates="coordinate", uselist=False)


class VehicleType(Base):
    __tablename__ = "vehicle_types"

    # id = Column(Integer, primary_key=True, autoincrement=True)
    _type = Column(String)
    color = Column(String)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    vehicle = relationship("Vehicle", back_populates="vehicle_type", uselist=False)
