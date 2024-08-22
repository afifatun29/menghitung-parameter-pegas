# Program Menghitung Parameter Pegas

def hitung_gaya(k, x):
    """
    Menghitung gaya berdasarkan Hukum Hooke.
    F = k * x
    """
    F = k * x
    return F

def hitung_perpindahan(F, k):
    """
    Menghitung perpindahan berdasarkan Hukum Hooke.
    x = F / k
    """
    x = F / k
    return x

def hitung_konstanta(F, x):
    """
    Menghitung konstanta pegas.
    k = F / x
    """
    if x == 0:
        return None
    k = F / x
    return k

def hitung_energi_potensial(k, x):
    """
    Menghitung energi potensial elastis.
    E_p = 1/2 * k * x^2
    """
    E_p = 0.5 * k * (x ** 2)
    return E_p

def main():
    print("=== Program Menghitung Parameter Pegas ===")
    print("Pilih perhitungan:")
    print("1. Hitung Gaya Pegas (F)")
    print("2. Hitung Perpindahan Pegas (x)")
    print("3. Hitung Konstanta Pegas (k)")
    print("4. Hitung Energi Potensial Elastis")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        k = float(input("Masukkan konstanta pegas (k) dalam N/m: "))
        x = float(input("Masukkan perpindahan (x) dalam meter: "))
        F = hitung_gaya(k, x)
        print(f"Gaya yang dihasilkan pegas adalah: {F:.2f} N")

    elif pilihan == '2':
        F = float(input("Masukkan gaya yang diberikan (F) dalam N: "))
        k = float(input("Masukkan konstanta pegas (k) dalam N/m: "))
        x = hitung_perpindahan(F, k)
        print(f"Perpindahan pegas adalah: {x:.2f} meter")

    elif pilihan == '3':
        F = float(input("Masukkan gaya yang diberikan (F) dalam N: "))
        x = float(input("Masukkan perpindahan (x) dalam meter: "))
        k = hitung_konstanta(F, x)
        if k is None:
            print("Perpindahan tidak boleh nol!")
        else:
            print(f"Konstanta pegas adalah: {k:.2f} N/m")

    elif pilihan == '4':
        k = float(input("Masukkan konstanta pegas (k) dalam N/m: "))
        x = float(input("Masukkan perpindahan (x) dalam meter: "))
        E_p = hitung_energi_potensial(k, x)
        print(f"Energi potensial elastis adalah: {E_p:.2f} joule")

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
