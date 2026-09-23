class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(300, 30)

print('maxspeed', modelx.max_speed)
print('mileage', modelx.mileage)