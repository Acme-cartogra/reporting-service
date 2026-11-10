from fastapi import FastAPI

app = FastAPI(title="reporting-service", version="1.0.0")

@app.get("/actuator/health")
def health(): return {"status": "UP"}

@app.get("/reportings")
def route_0(): return {"status": "ok"}

@app.post("/reportings")
def route_1(): return {"status": "ok"}

@app.get("/reportings/{id}")
def route_2(): return {"status": "ok"}
