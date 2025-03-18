import numpy as np
from scipy.io.wavfile import write

#This function creates a sine wave for any given frequency.
def generate_frequency(frequency: float, duration: float = 1.0, sample_rate: int = 44100):
    """Generate a WAV file for a given frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return (wave * 32767).astype(np.int16)  #This will convert to 16-bit PCM.


# Inputs:
#     frequencies: A list of frequencies (e.g., [440, 550, 660]).
# Output:
#     A single NumPy array that combines all those tones.
def blend_frequencies(frequencies: list, duration: float = 1.0, sample_rate: int = 44100):
    """Combine multiple frequencies into a single waveform."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Average the waves for a balanced mix
    wave = sum(0.5 * np.sin(2 * np.pi * f * t) for f in frequencies) / len(frequencies)
    return (wave * 32767).astype(np.int16)