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

duck = Bird('little_duck')
duck.fly()