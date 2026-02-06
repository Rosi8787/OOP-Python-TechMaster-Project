print("\n\n" + "="*60)
print("LATIHAN 3: Pewarisan (Inheritance)")
print("="*60)

class Hero3:
    """Parent class untuk semua hero"""
    
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)
    
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

class Mage(Hero3):
    """Child class: Mage dengan skill khusus"""
    
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana
    
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    
    def skill_fireball(self, lawan):
        """Skill khusus Mage: Fireball dengan damage 2x"""
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

# Demo Inheritance
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero3("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)