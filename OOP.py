
class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self,name = None, age = None, isHappy= None ):
        self.set_data(name, age , isHappy)
        self.get_data()
    def set_data(self, name = None, age = None , isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age:', self.age, 'Happy:', self.isHappy )

cat1 = Cat('Gucci', 2 , True)
# cat1.set_data('Gucci', 3, True)
# cat1.name = 'Gucci'
# cat1.age = 3
# cat1.isHappy = True
cat2 = Cat('Jopaaa', 2 ,False)
# cat2.set_data('Jopaaa', 2, False)
cat1.set_data()
cat1.get_data()
# cat1.get_data()
# cat2.get_data()


array = ['1:0','2:4','3:5','4:8']
print(array[2][0])