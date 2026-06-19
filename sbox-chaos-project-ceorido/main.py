from sbox.generate_sbox import generate_sbox

def main():

    sbox = generate_sbox()

    print("\n===== HASIL S-BOX =====\n")

    for i in range(0, 256, 16):

        row = sbox[i:i+16]

        print(" ".join(f"{x:3}" for x in row))
        
    print("\nJumlah elemen:", len(sbox))


if __name__ == "__main__":
    main()