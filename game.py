import random
from enum import Enum

class Unit(Enum):
    SOLDIER = 1
    TANK = 5
    HELICOPTER = 3

class Army:
    def __init__(self, name):
        self.name = name
        self.soldiers = 50
        self.tanks = 5
        self.helicopters = 3
        self.health = 100
        self.gold = 1000
    
    def display_army(self):
        print(f"\n--- جيش {self.name} ---")
        print(f"الجنود: {self.soldiers}")
        print(f"الدبابات: {self.tanks}")
        print(f"الطائرات العمودية: {self.helicopters}")
        print(f"الصحة: {self.health}")
        print(f"الذهب: {self.gold}")
    
    def buy_unit(self, unit_type):
        costs = {
            Unit.SOLDIER: 50,
            Unit.TANK: 300,
            Unit.HELICOPTER: 200
        }
        
        if self.gold >= costs[unit_type]:
            self.gold -= costs[unit_type]
            if unit_type == Unit.SOLDIER:
                self.soldiers += 1
            elif unit_type == Unit.TANK:
                self.tanks += 1
            elif unit_type == Unit.HELICOPTER:
                self.helicopters += 1
            print(f"✅ تم شراء {unit_type.name}!")
            return True
        else:
            print(f"❌ لا توجد أموال كافية! تحتاج {costs[unit_type]} ذهب")
            return False
    
    def attack(self, enemy):
        total_damage = (self.soldiers * 1) + (self.tanks * 5) + (self.helicopters * 3)
        damage = random.randint(int(total_damage * 0.7), total_damage)
        
        enemy.health -= damage
        print(f"\n⚔️ هجم {self.name}!")
        print(f"💥 الضرر: {damage}")
        print(f"❤️ صحة {enemy.name} المتبقية: {enemy.health}")
        
        return enemy.health <= 0

class WarGame:
    def __init__(self):
        self.player1 = Army("الجيش الأول")
        self.player2 = Army("الجيش الثاني")
        self.turn = 1
    
    def display_menu(self):
        print("\n" + "="*40)
        print(f"الدور #{self.turn}")
        print("="*40)
        print("1. اشتري جنود (50 ذهب)")
        print("2. اشتري دبابة (300 ذهب)")
        print("3. اشتري طائرة عمودية (200 ذهب)")
        print("4. عرض الجيش")
        print("5. هاجم العدو")
        print("6. انتهي الدور")
        print("="*40)
    
    def play(self):
        print("🎮 مرحباً بك في لعبة الحرب!")
        print("="*40)
        
        while self.player1.health > 0 and self.player2.health > 0:
            # دور اللاعب الأول
            print(f"\n🎯 دور {self.player1.name}")
            self.player1.display_army()
            
            while True:
                self.display_menu()
                choice = input("اختر (1-6): ").strip()
                
                if choice == "1":
                    self.player1.buy_unit(Unit.SOLDIER)
                elif choice == "2":
                    self.player1.buy_unit(Unit.TANK)
                elif choice == "3":
                    self.player1.buy_unit(Unit.HELICOPTER)
                elif choice == "4":
                    self.player1.display_army()
                elif choice == "5":
                    if self.player1.attack(self.player2):
                        print(f"\n🏆 {self.player1.name} فاز!")
                        return
                    break
                elif choice == "6":
                    break
                else:
                    print("❌ اختيار غير صحيح!")
            
            # دور اللاعب الثاني
            print(f"\n🎯 دور {self.player2.name}")
            self.player2.display_army()
            
            while True:
                self.display_menu()
                choice = input("اختر (1-6): ").strip()
                
                if choice == "1":
                    self.player2.buy_unit(Unit.SOLDIER)
                elif choice == "2":
                    self.player2.buy_unit(Unit.TANK)
                elif choice == "3":
                    self.player2.buy_unit(Unit.HELICOPTER)
                elif choice == "4":
                    self.player2.display_army()
                elif choice == "5":
                    if self.player2.attack(self.player1):
                        print(f"\n🏆 {self.player2.name} فاز!")
                        return
                    break
                elif choice == "6":
                    break
                else:
                    print("❌ اختيار غير صحيح!")
            
            self.turn += 1
        
        if self.player1.health <= 0:
            print(f"\n🏆 {self.player2.name} فاز!")
        else:
            print(f"\n🏆 {self.player1.name} فاز!")

if __name__ == "__main__":
    game = WarGame()
    game.play()
