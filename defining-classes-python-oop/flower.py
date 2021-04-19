class Flower:

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
        self.watering = 0

    def water(self, quantity):
        self.watering += quantity
        self.is_happy = self.watering >= self.water_requirements

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"

        return f"{self.name} is not happy"

# Test code
# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(100)
# print(flower.status())