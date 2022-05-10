class Animal:
    def __init__(self, name):
        self.name = name

    def animal_name(self):
        print(self.name)
    def eat(self):
        print("Animal eat method is called.")

class Bird(Animal):
    def fly(self):
        print("Bird fly method is called.")

class Duck(Bird):
    def call(self):
        print("quack")

if __name__ == '__main__':
    duck = Bird('little_cat')
    duck.fly()
    print("CAT!")
    print('DOG2!')
