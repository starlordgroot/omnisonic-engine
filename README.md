# OmniSonic Core

## Overview
OmniSonic Core is the backend engine powering the OmniSonic platform, handling real-time frequency synthesis, AI-driven harmonic analysis, and WebSocket-based sound processing. It provides the foundation for generating and manipulating sound waves, ensuring high-fidelity output and seamless communication with the front-end UI.

## Features
- **Real-Time Frequency Generation** – Produces accurate frequency outputs with minimal latency
- **AI-Powered Harmonic Analysis** – Intelligent frequency blending for enhanced user experience
- **WebSockets for Live Audio Control** – Instant response to UI-based input changes
- **Lossless Audio Processing** – Ensures precise sound reproduction using WAV format
- **Modular API Design** – REST and WebSocket interfaces for external integrations
- **Secure and Scalable** – Built with Python FastAPI for high-performance handling

## Tech Stack
- **FastAPI** – High-performance API framework
- **NumPy/SciPy** – Audio signal processing
- **WebSockets** – Real-time bi-directional communication
- **FFmpeg** – Audio encoding and manipulation
- **Redis (Optional)** – Caching for optimized processing
- **Docker (Optional)** – Containerization for deployment

## Installation & Setup

### Prerequisites
- Python 3.9+
- Pipenv or virtualenv for dependency management
- FFmpeg installed on the system

### Clone and Install Dependencies
```
git clone git@github.com:yourusername/OmniSonic-Core.git
cd OmniSonic-Core
pip install -r requirements.txt
```

### Run the Backend
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at `http://localhost:8000`

## Directory Structure
```
/src
  /services        # Core frequency synthesis and processing logic
  /api            # REST & WebSocket endpoints
  /utils          # Helper functions and processing utilities
/tests            # Unit and integration tests
requirements.txt  # Dependencies
README.md        # Documentation
```

## API Endpoints
### WebSocket Connection
```
ws://localhost:8000/ws/audio-stream/
```
- Streams real-time frequency data for visualization
- Receives UI input and adjusts audio output instantly

### Example REST Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/generate-frequency/` | Generates a single frequency tone |
| `POST` | `/mix-frequencies/` | Combines multiple frequency layers |
| `POST` | `/ai/suggest-frequencies/` | AI-driven harmonic recommendations |

## Roadmap
- Implement **adaptive AI sound recommendations**
- Introduce **MIDI & external instrument support**
- Expand **high-performance real-time synthesis capabilities**
- Optimize **scalability for multi-user experiences**

## Contributing
OmniSonic Core is a private repository, but internal contributions and improvements are welcome. For feature requests, open an issue.

## License
Proprietary - Not for public use.

## Related Repositories
- **OmniSonic UI** (Frontend): `https://github.com/yourusername/OmniSonic-UI`
