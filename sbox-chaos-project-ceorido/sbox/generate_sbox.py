from chaotic.logistic_map import logistic_map


def generate_sbox(x0=0.5, r=3.99, iterations=10000):

    # Generate chaotic sequence
    chaotic_sequence = logistic_map(x0, r, iterations)

    # Tempat penyimpanan S-Box
    sbox = []

    for x in chaotic_sequence:

        # Konversi chaos ke integer 0-255
        value = int(x * 10**6) % 256

        # Pastikan unik (bijektif)
        if value not in sbox:
            sbox.append(value)

        # Berhenti jika sudah 256 elemen
        if len(sbox) == 256:
            break

    return sbox


if __name__ == "__main__":

    sbox = generate_sbox()

    print("Jumlah elemen S-Box:", len(sbox))

    print("\n10 Elemen Pertama:")
    print(sbox[:10])

    # Cek bijektif
    if len(set(sbox)) == 256:
        print("\nS-Box Bijektif ✅")
    else:
        print("\nS-Box Tidak Valid ❌")