from pydantic import BaseModel


class VehicleTypeBase(BaseModel):
    _type: str
    color: str


class VehicleTypeCreate(VehicleTypeBase):
    pass


class VehicleType(VehicleTypeBase):
    # id: int

    # vehicle_id: int

    class Config:
        from_attributes = True


class CoordinateBase(BaseModel):
    latitude: float
    longitude: float


class CoordinateCreate(CoordinateBase):
    pass


class Coordinate(CoordinateBase):
    # id: int

    # vehicle_id: int

    class Config:
        from_attributes = True


class VehicleBase(BaseModel):
    heading: float
    sleepiness: int


class VehicleCreate(VehicleBase):
    vehicle_type: VehicleTypeCreate
    coordinate: CoordinateCreate


class Vehicle(VehicleBase):
    id: int
    vehicle_type: VehicleType
    coordinate: Coordinate

    class Config:
        from_attributes = True
