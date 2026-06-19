import streamlit as st
import numpy as np


def walsh_transform(boolean_function):

    size = len(boolean_function)

    walsh = np.zeros(size)

    for w in range(size):

        total = 0

        for x in range(size):

            fx = boolean_function[x]

            wx = bin(w & x).count("1") % 2

            total += (-1) ** (fx ^ wx)

        walsh[w] = total

    return walsh


def calculate_boolean_nl(boolean_function):

    walsh = walsh_transform(boolean_function)

    max_walsh = np.max(np.abs(walsh))

    nl = 128 - (max_walsh / 2)

    return nl


def calculate_bic_nl(sbox):

    bic_nl_values = []

    # pasangan bit output
    for bit1 in range(8):

        for bit2 in range(bit1 + 1, 8):

            boolean_function = []

            for x in range(256):

                b1 = (sbox[x] >> bit1) & 1
                b2 = (sbox[x] >> bit2) & 1

                xor_bit = b1 ^ b2

                boolean_function.append(xor_bit)

            nl = calculate_boolean_nl(boolean_function)

            bic_nl_values.append(
                {
                    "pair": (bit1, bit2),
                    "nl": nl
                }
            )

    return bic_nl_values


if __name__ == "__main__":

    from load_sbox import load_sbox

    sbox = load_sbox(
    "output/sbox_optimized.txt"
    )

    results = calculate_bic_nl(sbox)

    print("=== BIC-NL RESULTS ===\n")

    total_nl = 0

    for result in results:

        pair = result["pair"]
        nl = result["nl"]

        total_nl += nl

        print(
            f"Bit {pair[0]} XOR Bit {pair[1]}"
            f" -> NL = {nl}"
        )

    avg_bic_nl = total_nl / len(results)

    print("\n======================")
    print(f"Average BIC-NL = {avg_bic_nl:.2f}")