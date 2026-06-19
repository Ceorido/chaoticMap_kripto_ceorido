import matplotlib.pyplot as plt

def logistic_map(x0, r, iterations):
    x = x0
    sequence = []

    for _ in range(iterations):
        x = r * x * (1 - x)
        sequence.append(x)

    return sequence


if __name__ == "__main__":

    x0 = 0.5
    r = 3.99
    iterations = 100

    chaotic_sequence = logistic_map(x0, r, iterations)

    print("Chaotic Sequence:")
    print(chaotic_sequence[:10])

    # Visualisasi
    plt.plot(chaotic_sequence)
    plt.title("Logistic Chaotic Map")
    plt.xlabel("Iterasi")
    plt.ylabel("Nilai Chaos")
    plt.grid(True)
    plt.show()