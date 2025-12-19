from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze")
def analyze(features: dict):
    # return decision + explanation
    return result
