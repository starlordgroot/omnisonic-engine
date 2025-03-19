import json
from fastapi import APIRouter, WebSocket
from src.services.audio_processing import generate_frequency

router = APIRouter()

# Dictionary to store active WebSocket connections
active_connections = set()


@router.websocket("/ws/audio-stream")
async def audio_stream(websocket: WebSocket):
    """Handles real-time audio streaming over WebSockets."""
    await websocket.accept()
    active_connections.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            frequency = message.get("frequency", 440)  # Default to 440Hz if not provided

            # Generate frequency and send audio data
            audio_wave = generate_frequency(frequency)
            await websocket.send_bytes(audio_wave.tobytes())

    except Exception as e:
        print(f"WebSocket Error: {e}")
    finally:
        active_connections.remove(websocket)