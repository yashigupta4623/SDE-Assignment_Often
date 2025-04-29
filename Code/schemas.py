from pydantic import BaseModel
from typing import List, Optional

class ActivitySchema(BaseModel):
    name: str
    description: Optional[str] = None

class TransferSchema(BaseModel):
    from_location: str
    to_location: str

class AccommodationSchema(BaseModel):
    hotel_name: str
    address: str

class DaySchema(BaseModel):
    day_number: int
    activities: List[ActivitySchema]
    transfers: List[TransferSchema]
    accommodations: List[AccommodationSchema]

class ItineraryCreateSchema(BaseModel):
    name: str
    region: str
    nights: int
    days: List[DaySchema]
