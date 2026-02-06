print("\n\n" + "="*60)
print("LATIHAN 4: Enkapsulasi (Mengamankan Data HP)")
print("="*60)

class Hero4:
    """Hero dengan enkapsulasi: HP dilindungi dengan getter/setter"""
    
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # Private attribute
    
    def get_hp(self):
        """Getter: Cara resmi melihat HP"""
        return self.__hp
    
    def set_hp(self, nilai_baru):
        """Setter: Cara resmi mengubah HP dengan validasi"""
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru
    
    def diserang(self, damage):
        """Menerima damage dengan validasi HP"""
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# Demo Encapsulation
hero_x = Hero4("Layla", 100)
print("Mencoba set HP negatif (-50):")
hero_x.set_hp(-50)
print(f"HP setelah validasi: {hero_x.get_hp()}")

# Tugas Analisis 4.1: Percobaan Hacking
print("\n--- Tugas Analisis 4.1: Percobaan Hacking ---")
print(f"Akses paksa via name mangling: {hero_x._Hero4__hp}")

# Tugas Analisis 4.2: Tanpa validasi akan berbahaya
print("\n--- Tugas Analisis 4.2: Pentingnya Setter ---")
print("Tanpa setter, HP bisa jadi negatif atau terlalu besar (cheating!)")

