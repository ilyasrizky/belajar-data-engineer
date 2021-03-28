class kendaraan:
    bahan_bakar = "Bensin"

    def __init__(self, nama, warna, jumlah_roda):
        self.nama = nama
        self.warna = warna
        self.jumlah_roda = jumlah_roda

    def maju(self):
        print(self.nama, "sedang maju")

    def mundur(self):
        print(self.nama, "sedang mundur")

    @staticmethod
    def isi_bahan_bakar():
        print(kendaraan.bahan_bakar, "sedang diisi")


class mobil(kendaraan):
    pass


class pesawat(kendaraan):
    pass


mobil = kendaraan("Brio", "hitam", 4)
pesawat = kendaraan("garuda", "putih", 3)

mobil.maju()
pesawat.mundur()

mobil.isi_bahan_bakar()
pesawat.isi_bahan_bakar()
