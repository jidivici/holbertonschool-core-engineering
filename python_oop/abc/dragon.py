#!/usr/bin/env python3
"""Module that defines Animal, Dog, and Cat classes using ABC."""


class SwimMixin:
    """Module that defines Animal, Dog, and Cat classes using ABC."""

    def swim(self):
        """Swim the animal."""
        print("The creature swims!")


class FlyMixin:
    """Module that defines Animal, Dog, and Cat classes using ABC."""

    def fly(self):
        """Fly the animal."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Module that defines Animal, Dog, and Cat classes using ABC."""

    def roar(self):
        """Dragon the animal roars."""
        print("The dragon roars!")
