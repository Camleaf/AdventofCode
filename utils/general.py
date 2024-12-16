from dataclasses import dataclass
from abc import ABC, abstractmethod


def data_collect(year:int, day:int):
    with open(f"https://adventofcode.com/{year}/day/{day}/input","r") as file:
         return file.read()
