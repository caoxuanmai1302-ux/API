from fastapi import FastAPI
import requests

app = FastAPI(title="Environmental DSS API")

OPENAQ_URL = "https://api.openaq.org/v2/latest"

@app.get("/")
def home():
    return {"message": "API lấy dữ liệu môi trường đang chạy"}

@app.get("/get-air-quality")
def get_air_quality(city: str = "Ho Chi Minh City"):
    params = {
        "city": city,
        "limit": 5
    }

    response = requests.get(OPENAQ_URL, params=params)
    data = response.json()

    results = []

    for item in data["results"]:
        location = item["location"]
        for m in item["measurements"]:
            results.append({
                "location": location,
                "parameter": m["parameter"],
                "value": m["value"],
                "unit": m["unit"]
            })

    return {
        "city": city,
        "data": results
    }
