import numpy as np
import sounddevice as sd

#This function creates a sine wave for any given frequency. Sin is the most general os
def generate_frequency(frequency: float, duration: float = 1.0, sample_rate: int = 44100):
    """Generate a sine wave for a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def play_tone(frequency: float, duration: float = 1.0, sample_rate: int = 44100):
    """Generate and play a sine wave for the given frequency and duration."""
    wave = generate_frequency(frequency, duration, sample_rate)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

# Inputs:
#     frequencies: A list of frequencies (e.g., [440, 550, 660]).
# Output:
#     A single NumPy array that combines all those tones.
def blend_frequencies(frequencies: list, duration: float = 1.0, sample_rate: int = 44100):
    """Combine multiple frequencies into a single waveform."""
    waves = [generate_frequency(f, duration, sample_rate) for f in frequencies]
    combined_wave = sum(waves) / len(waves)
    return combined_wave