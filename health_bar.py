'''As barras de vida devem ter as seguintes propriedades:
tamanho, max value, dynamic value, simbols for remaining and lost amount,
decorating barriers, colors.

Deverá ter 2 ações uma de atualizar o HP corrente e outro para desenhar o hp na tela'''

import os

os.system("") #é um hotfix para caso o terminal não printar cores corretamente

class HealthBar:
    '''Simbolos serão os mesmos para todas as barars portanto pode ser deifinido globalmente'''
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }
    
    def __init__(self, entity, lenght: int = 20, is_colored: bool = True, color: str = "") -> None:
        '''ao invés de definir max health e current_value definimos a entidade que ira atualizar os valores'''
        self.entity = entity
        self.lenght = lenght
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors['default']

    def update(self)-> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.lenght)
        lost_bars = self.lenght - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")