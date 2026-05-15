#!/usr/bin/env python3
"""Module that defines Dragon, fly, and swim classes using ."""

class SwimMixin:
    """Mixin providing swimming capability to classes."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")

class FlyMixin:
    """Mixin providing flying capability to classes."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying abilities."""

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
