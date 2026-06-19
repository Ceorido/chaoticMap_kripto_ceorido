def calculate_bic_sac(sbox):

    bic_sac_values = []

    # semua pasangan bit output
    for bit1 in range(8):

        for bit2 in range(bit1 + 1, 8):

            total_changes = 0
            total_tests = 0

            for x in range(256):

                original_bit1 = (sbox[x] >> bit1) & 1
                original_bit2 = (sbox[x] >> bit2) & 1

                original_xor = original_bit1 ^ original_bit2

                for input_bit in range(8):

                    modified_input = x ^ (1 << input_bit)

                    modified_bit1 = (
                        (sbox[modified_input] >> bit1) & 1
                    )

                    modified_bit2 = (
                        (sbox[modified_input] >> bit2) & 1
                    )

                    modified_xor = modified_bit1 ^ modified_bit2

                    if original_xor != modified_xor:
                        total_changes += 1

                    total_tests += 1

            bic_sac = total_changes / total_tests

            bic_sac_values.append(
                {
                    "pair": (bit1, bit2),
                    "bic_sac": bic_sac
                }
            )

    return bic_sac_values


if __name__ == "__main__":

    from load_sbox import load_sbox

    sbox = load_sbox(
    "output/sbox_optimized.txt"
    )

    results = calculate_bic_sac(sbox)

    print("=== BIC-SAC RESULTS ===\n")

    total = 0

    for result in results:

        pair = result["pair"]
        value = result["bic_sac"]

        total += value

        print(
            f"Bit {pair[0]} XOR Bit {pair[1]}"
            f" -> BIC-SAC = {value:.4f}"
        )

    average = total / len(results)

    print("\n======================")
    print(f"Average BIC-SAC = {average:.4f}")