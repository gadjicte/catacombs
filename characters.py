import weapons 
import armor as armor



class character:
    def __init__(self, name: str, health: int   ) -> None:
        self.name= name
        self.health= health
        self.max_health= health

        self.weapon = weapons.fist

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.hp, 0)
        print(f"health of {player.name} : {player.health}"
        f"health of {enemy.name} : {enemy.health}")
        input("# ")

    


                                                                    
class player(character):
    def __init__(self, name: str, health: int, damage: int) -> None:
        super().__init__(name, health, damage)
    

    def equip(self, weapon) -> None:     



class enemy(character): 



class knight(player):  



class goblin(enemy):
    
    

    
    

class necromancer(player):    





class archer(player):
