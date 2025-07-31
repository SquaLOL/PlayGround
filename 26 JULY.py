def missing(nums, s):
    word = s.lower().replace(' ',"")
    cont = [''] * len(s)
    if max(nums) > len(word):
        return "No mission today"
    for i, y in enumerate(nums):
        if nums[i] == y and len(cont) > y:
            cont[y] = word[y]
    return "".join(cont)

print(missing([0,3,5], "I love you"))

# for i, y in enumerate(nums):
#     if nums[i] == y and len(cont) > y:
#         cont[y] = word[y]
#     else:
#         return "No mission today"
#
# return "".join(cont)



def multiples(m, n) -> int:
    arr = []
    for i in range(1,m + 1):
        arr.append(n * i)
    return arr

print(multiples(3,5))

def new_multiples(m, n):
    return [n * i for i in range(1, m + 1)]



class Hero(object):
    def __init__(self, name='Hero', position='00', health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience
    def get_info(self):
        print('name:',self.name,'health:',self.health, 'experience:', self.experience,'position:',self.position,'damage:',self.damage,)

myHero = Hero('Kolau', 100)
myHero.get_info()


def remove_char(s):
    temp = ''
    for i in s:
       temp = s[1:-1:]
    return temp

print(remove_char('place'))






















