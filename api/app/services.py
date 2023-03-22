from api.app.prediction_model.predictor import PricePredictor
from api.app.schemas.payloads import InputData, OutputData
from api.app.configs import config_predict
from utils.utils import BASE_DIR
from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse

app = FastAPI()
router = APIRouter()
predictor = PricePredictor(BASE_DIR / config_predict["trained_file"])

@app.get("/")
async def status():
    response = {
        "HealthCheck": "Ok",
        "Version": config_predict["version"]}
    return JSONResponse(content=response, media_type="application/json")


@router.post("/predict", response_model=OutputData)
async def predict(request: InputData):
    try:
        prediction = predictor.predict(request)
        return OutputData(id=request.id, price_category=prediction)
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred while processing the request: {e}"}, status_code=500)
