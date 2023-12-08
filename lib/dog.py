#!/usr/bin/env python3
class Dog:
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed if breed else "Mutt"
