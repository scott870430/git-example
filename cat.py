from animal import Animal

class Cat(Animal):
    def call(self):
        print('Meow~')


if __name__ == '__main__':
    black = Cat('little_cat')
    black.call()
    print("cat!")