class Observer:
    def __init__(self):
        self._observers = []

    def update(self):
        raise NotImplementedError("Subclasses should implement this method")
