from weapons import fists
from health_bar import HealthBar

class Character:
    
    def __init__(self, name: str, health: int) -> None:
        '''Adicionar a funcionalidade de armadura/defesa'''
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists
    
    def attack(self, target) -> None:
        '''vida do alvo abaixa de acordo com o dano
        Posso adicionar a funcionalidade de defesa também para reduzir o dano'''
        target.health -= self.weapon.damage
        target.health = max(target.health, 0) #avoid health to go below zero
        target.health_bar.update()
        print(f'{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.damage}')

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        # a default weapon sao os fists
        self.default_weapon = self.weapon 
        self.health_bar = HealthBar(self, color='green')

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped a(n) {self.weapon.name}')

    def drop(self) -> None:
        '''Define a arma padrão caso drope a arma equipada'''
        print(f"{self.name} dropped the {self.weapon.name}")
        self.weapon = self.default_weapon

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')