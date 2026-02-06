print("\n\n" + "="*60)
print("LATIHAN 5: Abstraction & Interface")
print("="*60)

from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.
class GameUnit(ABC):
    
    @abstractmethod
    def serang(self, target):
        pass
    
    @abstractmethod
    def info(self):
        pass

# 2. Implementasi pada Class Konkret
class Hero5(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    # Kita WAJIB membuat method serang, kalau tidak akan Error
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")
    
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
    
    # Implementasi serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

# -- Uji Coba --
print("\nMencoba membuat objek dari class abstrak:")
print("# unit = GameUnit()  # Akan ERROR!")

h = Hero5("Alucard")
m = Monster("Serigala")

print("\nMemanggil method info():")
h.info()
m.info()

print("\nMemanggil method serang():")
h.serang("Goblin")
m.serang("Petualang")

print("\n" + "="*60)
print("--- TUGAS ANALISIS 5 ---")
print("="*60)