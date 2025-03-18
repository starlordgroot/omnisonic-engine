from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI(title="OmniSonic Core")

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "OmniSonic Backend Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)