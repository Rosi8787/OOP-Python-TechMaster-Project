print("\n\n" + "="*60)
print("LATIHAN 6: Polymorphism (Fleksibilitas Interaksi)")
print("="*60)

# Parent Class
class Hero6:
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self):
        print("Hero menyerang dengan tangan kosong.")

# Child Class 1
class Mage6(Hero6):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

# Child Class 2
class Archer(Hero6):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

# Child Class 3
class Fighter(Hero6):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

# -- Penerapan Polymorphism --
# Kita punya daftar hero campuran
pasukan = [
    Mage6("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage6("Gord")
]

print("\n--- PERANG DIMULAI ---")
# Satu perintah loop, tapi respon berbeda-beda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()

print("\n" + "="*60)
print("--- TUGAS ANALISIS 6 ---")
print("="*60)

print("\n1. UJI SKALABILITAS (Kemudahan Menambah Fitur)")
print("-" * 60)

# Membuat class baru Healer
class Healer(Hero6):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

# Menambahkan Healer ke pasukan
print("\nMenambahkan class Healer tanpa mengubah kode loop:")
pasukan_baru = [
    Mage6("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes"),  # Class baru ditambahkan
    Mage6("Gord")
]

print("\n--- PERANG DENGAN HEALER ---")
for pahlawan in pasukan_baru:
    pahlawan.serang()