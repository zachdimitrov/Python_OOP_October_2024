from project.animal import Animal
from project.mammal import Mammal
from project.reptile import Reptile
from project.bear import Bear
from project.snake import Snake
from project.lizard import Lizard

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
