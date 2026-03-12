import math
def main():
    
    class Hero:
        def __init__(self, name, base_attack, health = 100):
            self.name = name
            self.base_attack = base_attack
            self._health = health

        def get_health(self):
            return self._health

        def set_health(self, y):
            self._health += 15
            
        def attack(self, atk):
            self.atk = atk 
            
        def display_dmg(self):
            print(self.atk)

        def __str__(self):
            return f"Character: {self.name} | Health: {self._health}"
        
    class Warrior (Hero):
        def __init__(self, name, base_attack):
            Hero.__init__(self, name, base_attack)
            self.attack = 40
            self.name = name
            
        def attack(self, atk):
            self.atk = atk 
            
        
            
    class Mage (Hero):
        def __init__(self, name, base_attack):
            Hero.__init__(self, name, base_attack)
            self.attack = 30
            self.name = name
        
        def attack(self, atk):
            self.atk = atk 
        


    class Villain (Hero):
        def __init__(self, name, base_attack):
            Hero.__init__(self, name, base_attack)
            self.attack = 20
            self.name = name
            
        def attack(self, atk):
            self.atk = atk 
            


    Heroin = ["Ganon","Merlin"]   
    for i, char in enumerate(Heroin, start=1):
        print(f"Characters no. {i}: {char}")     
        
    char1 = Warrior("Ganon", 40)
    char2 = Mage("Merlin", 30)
    
    
    enemy = Villain("Jackmeoff", 20)
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        player = char1
    else:
        player = char2
        
    print(player)
    
    while True:



def calculate_total_damage(*dmg):
    total = sum(dmg)
    return total

if __name__ == "__main__":
    main()
