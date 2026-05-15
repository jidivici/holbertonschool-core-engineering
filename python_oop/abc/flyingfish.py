#!/usr/bin/env python3
"""Module that defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Prints swimming behavior of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Prints flying behavior of the bird."""
        print("The fish is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, combining fish and bird behaviors."""

    def fly(self):
        """Prints flying behavior of the flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints swimming behavior of the flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
