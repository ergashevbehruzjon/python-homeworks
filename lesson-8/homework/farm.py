class Animal:
    def __init__(self, name, age, sound):
        self.__name = name
        self.__age = age
        self.__sound = sound

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or name=='':
            raise ValueError(f"name cannot be {name}")
        self.__name=name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if not isinstance(age,int) or age<0:
            raise ValueError(f"age cannot be {age}")
        self.__age=age

    @property
    def sound(self):
        return self.__sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def __str__(self):
        return f"{type(self).__name__}({self.name}, {self.age}, {self.sound})"


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        print(f"{self.name} is producing milk")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        print(f"{self.name} laid an egg")

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")

    def shear(self):
        print(f"Sheared {self.name}")

cow = Cow("Mol", 5)
chicken = Chicken("Tovuq", 2)
sheep = Sheep("Qoy", 3)

cow.make_sound()
cow.eat()
cow.sleep()
cow.produce_milk()
print(cow)
print('-'*30)
chicken.make_sound()
chicken.eat()
chicken.sleep()
chicken.lay_egg()
print(chicken)
print('-'*30)
sheep.make_sound()
sheep.eat()
sheep.sleep()
sheep.shear()
print(sheep)