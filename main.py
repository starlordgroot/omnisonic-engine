from fastapi import FastAPI
from src.api.routes import router as api_router
from src.api.websocket import router as ws_router
import numpy as np
import sounddevice as sd
from src.utils.frequency_helper import generate_harmonic_frequencies
from src.services.audio_processing import blend_frequencies, play_tone

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

#Plays a frequency
@app.post("/play-tone")
async def play_tone_endpoint(frequency: float, duration: float = 1.0):
    """Endpoint to play a tone."""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()
    return {"message": f"Playing tone at {frequency} Hz for {duration} seconds"}

# Run the application if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
