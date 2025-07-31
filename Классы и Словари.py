
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def say_name(self,suffix):
        print(self.name + suffix)


person = Person('Nikolai' , 27 , 'Moscow')
person2 = Person('Patrick', 24, 'Talin')


person2.say_name("!")


person_slovar = {
    "name": "Patrick",
    "age": 27,
    "city": "KLD",
    "say_name": lambda: print("My name is Nikolai")

}

person_slovar["say_name"]()


