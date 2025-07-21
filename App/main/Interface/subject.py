class Subject:
    def __init__(self, name):
        self.name = name
        self.observer = []

    def adicionarObserver(self, observer):
        if observer not in self.observer:
            self.observer.append(observer)

    def notificarObserver(self):
        for observer in self.observer:
            observer.update()