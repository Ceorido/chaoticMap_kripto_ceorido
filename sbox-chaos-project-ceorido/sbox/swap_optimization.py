import random

from evaluation.sac import calculate_sac
from evaluation.nonlinearity import calculate_nonlinearity


def calculate_fitness(sbox):
    """
    Fitness Function
    Semakin besar semakin baik
    """

    sac = calculate_sac(sbox)

    nl_values = calculate_nonlinearity(sbox)

    avg_nl = sum(nl_values) / len(nl_values)

    # SAC ideal = 0.5
    sac_penalty = abs(sac - 0.5)

    fitness = avg_nl - (100 * sac_penalty)

    return fitness, avg_nl, sac


def optimize_sbox(initial_sbox, iterations=1000):

    best_sbox = initial_sbox.copy()

    best_fitness, best_nl, best_sac = calculate_fitness(best_sbox)

    print("=== INITIAL SBOX ===")
    print(f"NL  : {best_nl:.2f}")
    print(f"SAC : {best_sac:.4f}")
    print(f"FIT : {best_fitness:.4f}")

    for iteration in range(iterations):

        candidate = best_sbox.copy()

        # pilih dua posisi random
        i, j = random.sample(range(256), 2)

        # swap
        candidate[i], candidate[j] = candidate[j], candidate[i]

        fitness, avg_nl, sac = calculate_fitness(candidate)

        if fitness > best_fitness:

            best_sbox = candidate
            best_fitness = fitness

            best_nl = avg_nl
            best_sac = sac

            print(
                f"[ITER {iteration}] "
                f"FIT={best_fitness:.4f} "
                f"NL={best_nl:.2f} "
                f"SAC={best_sac:.4f}"
            )

    return best_sbox, best_fitness, best_nl, best_sac


if __name__ == "__main__":

    from sbox.generate_sbox import generate_sbox

    initial_sbox = generate_sbox()

    optimized_sbox, fitness, nl, sac = optimize_sbox(
        initial_sbox,
        iterations=1000
    )

    print("\n=== FINAL RESULT ===")
    print(f"Fitness : {fitness:.4f}")
    print(f"NL      : {nl:.2f}")
    print(f"SAC     : {sac:.4f}")

    with open("output/sbox_optimized.txt", "w") as f:

        for i in range(0, 256, 16):

            row = optimized_sbox[i:i+16]

            f.write(
                " ".join(f"{x:3}" for x in row)
                + "\n"
            )

    print("\nOptimized S-Box saved to:")
    print("output/sbox_optimized.txt")