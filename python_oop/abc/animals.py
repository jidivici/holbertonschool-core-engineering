#!/usr/bin/env python3
"""Module that defines Animal, Dog, and Cat classes using ABC."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""

    def __init__(self, name):
        """Initialize a new Animal.

        Args:
            name (str): The name of the animal.
        """
        self.name = name

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal.

        Returns:
            str: The sound of the animal.
        """


class Dog(Animal):
    """Defines a dog, inherits from Animal."""

    def __init__(self, name=""):
        """Initialize a new Dog."""
        super().__init__(name)

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Defines a cat, inherits from Animal."""

    def __init__(self, name=""):
        """Initialize a new Cat."""
        super().__init__(name)

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
