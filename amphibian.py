class landanimal:
    def __init__(self):
        super().__init__()
        self.walking_speed = 5

    def increase_walking_speed(self,how_much):
        self.walking_speed += how_much

class wateranimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10

    def increase_swimming_speed(self,how_much):
        self.swimming_speed += how_much

class Amphibian(landanimal,wateranimal):
    def __init__(self):
        super().__init__()


amphibian = Amphibian()
amphibian.increase_walking_speed(25)
amphibian.increase_swimming_speed(30)
print(amphibian.walking_speed)
print(amphibian.swimming_speed)



