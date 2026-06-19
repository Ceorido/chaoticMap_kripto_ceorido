def calculate_dap(sbox):

    max_count = 0

    best_dx = 0
    best_dy = 0

    # abaikan dx = 0
    for dx in range(1, 256):

        ddt = [0] * 256

        for x in range(256):

            dy = sbox[x] ^ sbox[x ^ dx]

            ddt[dy] += 1

        local_max = max(ddt)

        if local_max > max_count:

            max_count = local_max

            best_dx = dx
            best_dy = ddt.index(local_max)

    dap = max_count / 256

    return (
        dap,
        max_count,
        best_dx,
        best_dy
    )


if __name__ == "__main__":

    from load_sbox import load_sbox

    sbox = load_sbox(
        "output/sbox_optimized.txt"
    )

    dap, max_count, dx, dy = calculate_dap(sbox)

    print("\n=== DAP RESULT ===")

    print(f"Input Difference  : {dx}")
    print(f"Output Difference : {dy}")
    print(f"Max Count         : {max_count}")
    print(f"DAP               : {dap:.6f}")