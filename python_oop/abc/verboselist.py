#!/usr/bin/env python3
from abc import ABC


class VerboseList(list, ABC):

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended [{}] to the list.".format(len(items)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] to the list.".format(item))

    def pop(self, index=-1):
       print("Popped [{}] to the list.".format(self[index]))
       super().pop(self[index])
