from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def get_html(self):
        pass


class Button(Element):

    def __init__(self):
        self.html = "<button></button>"

    def get_html(self):
        return self.html


class Container(Element):

    def __init__(self):
        self.html = "<div></div>"

    def get_html(self):
        return self.html


class Audio(Element):

    def __init__(self):
        self.html = "<audio />"

    def get_html(self):
        return self.html


class Factory():

    @staticmethod
    def create_element(plan):
        try:
            if plan == "button":
                return Button()
            elif plan == "container":
                return Container()
            elif plan == "audio":
                return Audio()
            raise AssertionError("Invalid element type")
        except AssertionError as e:
            print(e)
