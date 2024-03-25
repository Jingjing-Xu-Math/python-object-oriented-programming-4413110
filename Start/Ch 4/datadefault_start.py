# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = 'No titil'
    author: str = 'No author'
    pages: int = 0
    price: float


b1=Book(price=6.0)
print(b1)
