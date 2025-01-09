# Abstract Base Classes (ABCs) enforce the implementation of abstract methods in derived classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")

# Instantiate objects
car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()
