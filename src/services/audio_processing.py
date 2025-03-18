import numpy as np
from scipy.io.wavfile import write

def generate_frequency(frequency: float, duration: float = 1.0, sample_rate: int = 44100):
    """Generate a WAV file for a given frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return (wave * 32767).astype(np.int16)  #This will convert to 16-bit PCM.