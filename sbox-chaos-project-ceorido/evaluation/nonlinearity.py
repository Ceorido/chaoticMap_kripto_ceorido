import numpy as np


def walsh_transform(boolean_function):

    n = len(boolean_function)

    walsh = np.zeros(n)

    for w in range(n):

        total = 0

        for x in range(n):

            fx = boolean_function[x]

            wx = bin(w & x).count("1") % 2

            total += (-1) ** (fx ^ wx)

        walsh[w] = total

    return walsh


def calculate_nonlinearity(sbox):

    n = 8

    nl_values = []

    for bit in range(8):

        boolean_function = []

        for x in range(256):

            bit_value = (sbox[x] >> bit) & 1

            boolean_function.append(bit_value)

        walsh = walsh_transform(boolean_function)

        max_walsh = np.max(np.abs(walsh))

        nl = (2 ** (n - 1)) - (max_walsh / 2)

        nl_values.append(nl)

    return nl_values


# ==================================
# WAJIB ADA BAGIAN INI
# ==================================

if __name__ == "__main__":

    print("NL FILE BERJALAN")

    from load_sbox import load_sbox

    sbox = load_sbox(
    "output/sbox_optimized.txt"
    )

    nl = calculate_nonlinearity(sbox)

    print("NL tiap bit:")
    print(nl)

    print(f"Rata-rata NL: {sum(nl)/len(nl):.2f}")