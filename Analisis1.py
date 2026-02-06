print("="*60)
print("LATIHAN 1: Membuat Class Hero")
print("="*60)

class Hero:
    """Class dasar untuk Hero dengan atribut dan method dasar"""
    
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

# Tugas Analisis 1: Mengubah atribut secara langsung
print("\n--- Tugas Analisis 1 ---")
hero1.hp = 500
print(f"HP hero1 setelah diubah: {hero1.hp}")
hero1.info()