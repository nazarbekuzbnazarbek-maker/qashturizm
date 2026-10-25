from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Qashqadaryo & Sirdaryo Tourism API",
    description="Qashqadaryo va Sirdaryo viloyatlari turizm ilovasi uchun backend API",
    version="1.0.0"
)

# Pydantic modellari
class Location(BaseModel):
    id: int
    title: str
    region: str  # "Qashqadaryo" yoki "Sirdaryo"
    category: str  # "Tarix", "Tabiat", "Gastronomiya", "Agroturizm"
    description: str
    image_url: str
    latitude: float
    longitude: float
    rating: float
    address: str

# Boshlang'ich test ma'lumotlari (Database bilan almashtiriladi)
LOCATIONS_DB: List[Location] = [
    Location(
        id=1,
        title="Oqsaroy Majmuasi",
        region="Qashqadaryo",
        category="Tarix",
        description="Amir Temur tomonidan bunyod etilgan muazzam saroy qoldiqlari.",
        image_url="https://images.unsplash.com/photo-1541781774459-bb2af2f05b55",
        latitude=39.0583,
        longitude=66.8277,
        rating=4.9,
        address="Shahrisabz shahri, Qashqadaryo"
    ),
    Location(
        id=2,
        title="Suvushshar Sharsharasi",
        region="Qashqadaryo",
        category="Tabiat",
        description="G'issar tog' tizmasidagi maftunkor tabiat va toza havo maskani.",
        image_url="https://images.unsplash.com/photo-1432405972618-c60b0225b8f9",
        latitude=38.8411,
        longitude=67.3102,
        rating=4.8,
        address="Kitob tumani, Qashqadaryo"
    ),
    Location(
        id=3,
        title="Sirdaryo Baliqchilik Restorani & Dam olish Zonasi",
        region="Sirdaryo",
        category="Gastronomiya",
        description="Sirdaryo daryosi bo'yidagi mashhur daryo baliqlari va hordiq chiqarish maskani.",
        image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        latitude=40.8436,
        longitude=68.6617,
        rating=4.7,
        address="Sirdaryo tumani, Sirdaryo"
    ),
    Location(
        id=4,
        title="Guliston Eko Parki",
        region="Sirdaryo",
        category="Agroturizm",
        description="Shahar markazidagi zamonaviy va yashil dam olish maskani.",
        image_url="https://images.unsplash.com/photo-1519331379826-f10be5486c6f",
        latitude=40.4897,
        longitude=68.7842,
        rating=4.5,
        address="Guliston shahri, Sirdaryo"
    )
]

@app.get("/")
def home():
    return {"message": "Qashqadaryo va Sirdaryo Turizm API tizimi ishlamoqda!"}

@app.get("/api/v1/locations", response_model=List[Location])
def get_locations(region: Optional[str] = None, category: Optional[str] = None):
    results = LOCATIONS_DB
    if region:
        results = [loc for loc in results if loc.region.lower() == region.lower()]
    if category:
        results = [loc for loc in results if loc.category.lower() == category.lower()]
    return results

@app.get("/api/v1/locations/{location_id}", response_model=Location)
def get_location_detail(location_id: int):
    for loc in LOCATIONS_DB:
        if loc.id == location_id:
            return loc
    raise HTTPException(status_code=404, detail="Maskan topilmadi")
