class Siswa:
    # Pembuatan wadah data siswa dan pengisian data siswa
    def __init__(self,nama,kelas,jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
        self.kelulusan = False
    
    def printdetailsiswa(self):
        print(f"""
          Nama: {self.nama}
          Kelas: {self.kelas}
          Jurusan: {self.jurusan}
        """)

    def statuskelulusan(self):
        print(f" Kelulusan: {"Lulus" if self.kelulusan else "Belum Lulus"} ")
        
# Pemanggilan kode untuk pembuatan wadah beserta penyerahan data
ilham = Siswa("Ilham Dida Zakaria","12","TKJ")

# Print atribut
print(ilham.nama)
print(ilham.kelas)
print(ilham.jurusan)

ilham.printdetailsiswa()

print(ilham.kelulusan)

ilham.statuskelulusan()

