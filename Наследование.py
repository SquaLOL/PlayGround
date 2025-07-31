class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print('Year:' , self.year, 'City: ', self.city)
class House(Building):
    pass
class Shop(Building):
    people = 0
    def __init__(self, people, year, city):
        super(Shop, self).__init__(year, city)
        self.people = people
    def get_info(self):
        super().get_info()
        print('People', self.people)

class School(Shop):
    pass

school = School(1,2000, 'KLD')
school.get_info()
house = Shop(1,2000,'Msk')
house.get_info()
shop = Building(1997, 'Kld')
shop.get_info()