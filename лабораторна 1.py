from abc import ABC, abstractmethod

# Наслідування: Базовий абстрактний клас
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # Закритий атрибут (інкапсуляція)
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_name(self):
        return self._name

# Похідні класи
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  # Закритий атрибут
    
    def make_sound(self):
        return "Woof!"
    
    def get_breed(self):
        return self.__breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color  # Закритий атрибут
    
    def make_sound(self):
        return "Meow!"
    
    def get_color(self):
        return self.__color

# Поліморфізм: створення колекції об'єктів
animals = [Dog("Rex", "Labrador"), Cat("Whiskers", "Black"), Dog("Buddy", "Beagle")]

# Виклик абстрактного методу для кожного об'єкта
for animal in animals:
    print(f"{animal.get_name()} says {animal.make_sound()}")
