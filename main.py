from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/vehicles/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle(db=db, vehicle=vehicle)


@app.get("/vehicles/", response_model=list[schemas.Vehicle])
def read_vehicles(
        latitude: float,
        longitude: float,
        latitude_delta: float,
        longitude_delta: float,
        limit: int = 100,
        db: Session = Depends(get_db)
    ):
    vehicles = crud.get_vehicles(db, latitude=latitude, longitude=longitude, latitude_delta=latitude_delta, longitude_delta=longitude_delta, limit=limit)
    return vehicles


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
