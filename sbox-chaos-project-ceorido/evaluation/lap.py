def parity(value):

    return bin(value).count("1") % 2


def calculate_lap(sbox):

    max_bias = 0

    best_input_mask = 0
    best_output_mask = 0

    # hindari mask 0
    for input_mask in range(1, 256):

        for output_mask in range(1, 256):

            count = 0

            for x in range(256):

                input_parity = parity(
                    x & input_mask
                )

                output_parity = parity(
                    sbox[x] & output_mask
                )

                if input_parity == output_parity:
                    count += 1

            bias = abs(count - 128)

            if bias > max_bias:

                max_bias = bias

                best_input_mask = input_mask
                best_output_mask = output_mask
    print("Max Bias =", max_bias)
    lap = max_bias / 256

    return (
        lap,
        best_input_mask,
        best_output_mask
    )


if __name__ == "__main__":

    from load_sbox import load_sbox

    sbox = load_sbox(
    "output/sbox_optimized.txt"
    )

    lap, input_mask, output_mask = calculate_lap(
        sbox
    )

    print("\n=== LAP RESULT ===")

    print(
        f"Input Mask  : {input_mask}"
    )

    print(
        f"Output Mask : {output_mask}"
    )

    print(
        f"LAP         : {lap:.6f}"
    )