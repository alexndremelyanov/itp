class Observer:
    def __init__(self):
        self.subs = set()

    def register(self, sub):
        self.subs.add(sub)

    def unregister(self, sub):
        self.subs.discard(sub)

    def dispatch(self, msg):
        for sub in self.subs:
            sub.update(msg)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
