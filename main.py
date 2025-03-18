from fastapi import FastAPI
from src.api.routes import router as api_router
from src.api.websocket import router as ws_router

# Create the FastAPI application instance
app = FastAPI(title="OmniSonic Core")

# Include standard REST API routes
app.include_router(api_router)

# Include WebSocket endpoints
app.include_router(ws_router)

# Root endpoint to confirm the API is running
@app.get("/")
async def root():
    return {"message": "OmniSonic Backend Running"}

# Run the application if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
