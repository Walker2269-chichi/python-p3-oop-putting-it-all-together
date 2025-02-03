#!/usr/bin/env python3

class Shoe:
    def __init__(self, size, color, brand):
        self.size = size
        self.color = color
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.color} Shoe (Size {self.size})"
