print("\n\n" + "="*60)
print("LATIHAN 2: Interaksi Antar Objek")
print("="*60)

class Hero2:
    """Hero dengan kemampuan menyerang dan diserang"""
    
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
    def serang(self, lawan):
        """Menyerang hero lawan"""
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)
    
    def diserang(self, damage):
        """Menerima damage dari lawan"""
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# Membuat hero
hero_a = Hero2("Layla", 100, 15)
hero_b = Hero2("Zilong", 120, 20)

# Pertarungan
print("\n--- Pertarungan Dimulai ---")
hero_a.serang(hero_b)
hero_b.serang(hero_a)

