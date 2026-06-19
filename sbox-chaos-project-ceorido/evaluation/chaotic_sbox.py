import math

def logistic_sine_map(
        x0=0.54321,
        r=3.99,
        iterations=256,
        discard=1000):

    x = x0

    for _ in range(discard):

        x = (
            r * x * (1 - x)
            + ((4 - r) *
               math.sin(math.pi * x))
            / 4
        )

        x = x % 1

    sequence = []

    for _ in range(iterations):

        x = (
            r * x * (1 - x)
            + ((4 - r) *
               math.sin(math.pi * x))
            / 4
        )

        x = x % 1

        sequence.append(x)

    return sequence


def generate_chaotic_sbox(
        x0=0.54321,
        r=3.99,
        discard=1000):

    sequence = logistic_sine_map(
        x0=x0,
        r=r,
        iterations=256,
        discard=discard
    )

    indexed = list(
        enumerate(sequence)
    )

    indexed.sort(
        key=lambda item: item[1]
    )

    sbox = [
        item[0]
        for item in indexed
    ]

    return sbox, sequence