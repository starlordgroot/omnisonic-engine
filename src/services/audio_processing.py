import numpy as np

#This function creates a sine wave for any given frequency. Sin is the most general os
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


def generate_harmonic_frequencies(base_frequency: float, num_intervals: int = 5):
    """
    Generate a list of harmonic frequencies above and below a base frequency.
    Args:
        base_frequency (float): The initial frequency in Hz.
        num_intervals (int): The number of intervals above and below the base frequency.
    Returns:
        list: A list of harmonic frequencies.
    """

    # Ratios for musical intervals
    ratios = [1, 2, 3 / 2, 4 / 3, 5 / 4, 6 / 5]

    harmonics = [base_frequency]  # Start with the base frequency
    for ratio in ratios[1:num_intervals + 1]:  # Generate harmonics up
        harmonics.append(base_frequency * ratio)
    for ratio in ratios[1:num_intervals + 1]:  # Generate harmonics down
        harmonics.append(base_frequency / ratio)

    return harmonics