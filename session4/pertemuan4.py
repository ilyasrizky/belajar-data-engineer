def pangkat_print(angka, pangkat=2):
    hasil = angka**pangkat
    print(hasil)

pangkat_print(2)
pangkat_print(3)
pangkat_print(4)


def print_harga_dibayar(jumlah_barang, harga_barang):
    harga_dibayar = jumlah_barang * harga_barang
    print(harga_dibayar)

print_harga_dibayar(3, 1000)
print_harga_dibayar(15, 15000)
print_harga_dibayar(50, 10000)

def gaji(nama, gaji=5000):
    print("Karyawan", nama, "memiliki gaji:", gaji)

gaji("Naruto", 7000)