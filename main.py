'''A principio gostaria de jogar no terminal'''
'''Posteriormente gostaria de implementar o pygame e implementar
comandos de atack(?), o atack ser um número aleatório entre 0 - X, sendo X o dano da arma
e a defesa defender entre 0 e X sendo X a armadura
Além de um 'IA'?'''

from character import Hero, Enemy
from weapons import short_bow, iron_sword 

hero = Hero(name="Super Drindao", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Algum Idiota", health=100, weapon= short_bow)

while hero.health and enemy.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    # print(f"Health of {hero.name}: {hero.health}")
    # print(f"Health of {enemy.name}: {enemy.health}")

    # hero.drop()
    #control flow pressionar enter para próxima ação
    input()
    
print(f"{hero.name} amassou!")