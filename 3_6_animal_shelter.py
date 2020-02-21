# question: An anumal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest"(based on arrival time)
# of all animals at the shelter, or they can select whether they would prefer a dog or a cat
# (and will receive the oldest animal of that type). They cannot select which specific animal
# they would like. Create a data sturctures to maintain this system and implement operations
# such as enqueue, dequeueAny, dequeueDog and dequeueCat. You may use the built-in LinkedList
# data structure.

from utils import Queue

class Animal(object):

    def __init__(self, id, type):
        self.type = type
        self.id = id

    def get_type(self):
        return self.type

    def __repr__(self):
        return "{} #{}".format(self.type, self.id)

class Dog(Animal):

    def __init__(self, id):
        super(Dog, self).__init__(id, "dog")

class Cat(Animal):

    def __init__(self, id):
        super(Cat, self).__init__(id, "cat")

class AnimalShelter:

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.arrival_time = 0

    def enqueue(self, animal):
        if animal.get_type() == 'dog':
            self.dogs.enqueue([self.arrival_time, animal])
        else:
            self.cats.enqueue([self.arrival_time, animal])
        self.arrival_time += 1

    def dequeueAny(self):
        if self.dogs.is_empty() and self.cats.is_empty():
            raise Exception("Animal Shelter is empty")
        if self.dogs.is_empty():
            return self.cats.dequeue()[1]
        if self.cats.is_empty():
            return self.dogs.dequeue()[1]

        t1, _ = self.dogs.peek()
        t2, _ = self.cats.peek()
        if t1 < t2:
            return self.dogs.dequeue()[1]
        else:
            return self.cats.dequeue()[1]

    def dequeueDog(self):
        if self.dogs.is_empty():
            raise Exception("There is no dogs in animal shelter")
        return self.dogs.dequeue()[1]

    def dequeueCat(self):
        if self.cats.is_empty():
            raise Exception("There is no cats in animal shelter")
        return self.cats.dequeue()[1]

    def display(self):
        print "Cats: ", self.cats
        print "Dogs: ", self.dogs

animal_shelter = AnimalShelter()
animal_shelter.enqueue(Dog(1))
animal_shelter.enqueue(Cat(1))
animal_shelter.enqueue(Dog(2))
animal_shelter.enqueue(Dog(3))
animal_shelter.enqueue(Dog(4))
print animal_shelter.dequeueAny()
animal_shelter.enqueue(Cat(2))
animal_shelter.enqueue(Cat(3))
print animal_shelter.dequeueDog()
print animal_shelter.dequeueCat()
animal_shelter.display()