from fastapi import FastAPI, HTTPException
import util
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model và danh sách quận vào RAM ngay khi bật server
    print("Starting server")
    util.load_saved_artifacts()
    yield
    print("Shutdown")

app = FastAPI(
    title="Vietnam Housing Price",
    description="API use RandomForestRegressor for predicting price",
    version="1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

class HouseInput(BaseModel):
    area: float
    frontage: float
    access_road: float
    floors: int
    bedrooms: int
    bathrooms: int
    direction: str 
    balcony: str 
    district: str   

@app.get("/get_district_names")
def _get_district_names():
    response = {
        'districts': util.get_district_names()
    }
    #print(util.get_district_names())
    return response

@app.get("/get_direction_names")
def _get_direction_names():
    response = {
        'directions': util.get_direction_names()
    }
    return response

@app.get("/get_balcony_names")
def _get_balcony_names():

    response = {
        'balcony directions': util.get_balcony_names()
    }
    return response

@app.post("/predict_house_price")
def predict_price(item: HouseInput):
    
    try:
        price = util.get_estimated_price(
            item.area, 
            item.frontage, 
            item.access_road, 
            item.floors, 
            item.bedrooms, 
            item.bathrooms, 
            item.direction, 
            item.balcony, 
            item.district
        )
        
        # Trả về kết quả
        return {
            "price": price 
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import uvicorn
    #print(get_district_names())
    uvicorn.run("server:app", host="127.0.0.1", port=7000, reload=True)