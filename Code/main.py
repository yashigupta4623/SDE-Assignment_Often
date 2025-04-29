from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from models import Itinerary, Day, Activity, Accommodation, Transfer
from schemas import ItineraryCreateSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/itineraries/")
def create_itinerary(payload: ItineraryCreateSchema, db: Session = Depends(get_db)):
    itinerary = Itinerary(name=payload.name, region=payload.region, nights=payload.nights)
    for d in payload.days:
        day = Day(day_number=d.day_number)
        day.activities = [Activity(**a.dict()) for a in d.activities]
        day.transfers = [Transfer(**t.dict()) for t in d.transfers]
        day.accommodations = [Accommodation(**acc.dict()) for acc in d.accommodations]
        itinerary.days.append(day)
    db.add(itinerary)
    db.commit()
    db.refresh(itinerary)
    return {"id": itinerary.id, "message": "Itinerary created successfully."}

@app.get("/itineraries/{itinerary_id}")
def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    itinerary = db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

@app.get("/recommendations/{nights}")
def get_recommendations(nights: int, db: Session = Depends(get_db)):
    itineraries = db.query(Itinerary).filter(Itinerary.nights == nights).all()
    if not itineraries:
        raise HTTPException(status_code=404, detail="No recommendations available")
    return itineraries
