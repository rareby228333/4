import random


class pet:
    def __init__(self, name="sobaka po imeni vasya"):
        self.name = name
        self.satiety = 100
        self.gladness = 50
        self.health = 100

    def eat(self):
        self.satiety += 10
        self.health += 5

    def play(self):
        self.satiety -= 5
        injured = random.randint(1, 5)

        if injured == 3:
            self.health -= 10
        elif injured == 4:
            self.health -= 20
        elif injured == 5:
            self.health -= 50
            major_injured = random.randint(1, 100)
            if major_injured == 100:
                self.health -= 99999999999999
                print("my dog is dead due to major injure and blood loss")


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = None

    def dog_death_depression(self):
        if self.pet.health <= 0:
            print("my dog is dead... i lost him...")
            self.gladness -= 9999999999999

    def take_care_of_pet(self):
        if self.pet.satiety > 60:
            self.pet.eat()
            print("Feeding the pet")
        else:
            self.pet.play()
            print("Playing with the pet")
        self.gladness += 5

    def get_pet(self):
        self.pet = pet()
        print("i got a dog!")

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()
            return

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety < 100:
                self.satiety += 5
                self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
            return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
            return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"{f'Today the {day} of {self.name} life':=^50}")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        print(f"Car fuel: {self.car.fuel}")
        print(f"Car strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if self.pet is None:
            self.get_pet()
        else:
            self.take_care_of_pet()
            self.dog_death_depression()

        if not self.is_alive():
            return False

        if self.home is None:
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f"I got a job {self.job.job} with salary {self.job.salary}")

        self.days_indexes(day)

        dice = random.randint(1, 4)

        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping("delicacies")

        return True


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        print("The car cannot move")
        return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


nick = Human(name="Nick")

for day in range(1, 9999):
    if not nick.live(day):
        break
