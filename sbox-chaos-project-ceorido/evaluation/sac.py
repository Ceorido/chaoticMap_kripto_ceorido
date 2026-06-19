def count_bit_changes(a, b):

    xor = a ^ b

    return bin(xor).count("1")


def calculate_sac(sbox):

    total_changes = 0
    total_tests = 0

    for x in range(256):

        original_output = sbox[x]

        for bit in range(8):

            modified_input = x ^ (1 << bit)

            modified_output = sbox[modified_input]

            changes = count_bit_changes(
                original_output,
                modified_output
            )

            total_changes += changes

            total_tests += 8

    return total_changes / total_tests


# ==================================
# WAJIB ADA BAGIAN INI
# ==================================

if __name__ == "__main__":

    print("SAC FILE BERJALAN")

    from load_sbox import load_sbox

    sbox = load_sbox(
    "output/sbox_optimized.txt"
    )

    sac = calculate_sac(sbox)

    print(f"SAC Value: {sac:.4f}")