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