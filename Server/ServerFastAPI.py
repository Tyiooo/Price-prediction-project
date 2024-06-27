from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup_event():
    util.load_saved_artifacts()

@app.get('/get_location_names')
async def get_location_names():
    return {'locations': util.get_location_names()}

@app.post('/predict_home_price')
async def predict_home_price(request: Request):
    try:
        form = await request.form()
        total_sqft = float(form['total_sqft'])
        location = form['location']
        bhk = int(form['bhk'])
        bath = int(form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        return {'estimated_price': estimated_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
