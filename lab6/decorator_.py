from abc import ABC
import json


class Type(ABC):
    def __str__(self):
        raise Exception()


class List(Type):
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return " ".join(self.list)


class JSON(Type):
    def __init__(self, json):
        self.json = json

    def __str__(self):
        return json.dumps(self.json)
