from sqlalchemy.orm import Session

import models, schemas


def get_vehicles(
        db: Session,
        latitude: float,
        longitude: float,
        latitude_delta: float,
        longitude_delta: float,
        limit: int = 100
    ):
    
    return db.query(models.Vehicle).\
        filter(
            models.Vehicle.coordinate.latitude >= latitude - latitude_delta and
            models.Vehicle.coordinate.latitude <= latitude + latitude_delta and
            models.Vehicle.coordinate.longitude >= longitude - longitude_delta and
            models.Vehicle.coordinate.longitude <= longitude + longitude_delta
        ).\
        limit(limit).all()


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle_type = models.VehicleType(**vehicle.vehicle_type.dict())
    db_coordinate = models.Coordinate(**vehicle.coordinate.dict())

    db_vehicle = models.Vehicle(
        heading=vehicle.heading,
        sleepiness=vehicle.sleepiness,
        vehicle_type=db_vehicle_type,
        coordinate=db_coordinate
    )
    
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle
