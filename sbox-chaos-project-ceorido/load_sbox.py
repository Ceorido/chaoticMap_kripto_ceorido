def load_sbox(filename):

    sbox = []

    with open(filename, "r") as f:

        for line in f:

            numbers = line.split()

            sbox.extend(
                [int(x) for x in numbers]
            )

    return sbox


if __name__ == "__main__":

    sbox = load_sbox(
        "output/sbox_optimized.txt"
    )

    print("Jumlah elemen:", len(sbox))

    print(sbox[:10])