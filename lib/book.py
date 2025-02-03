#!/usr/bin/env python3
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
        else:
            raise ValueError("Book is already checked out")

    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
        else:
            raise ValueError("Book is not checked out")

    
        