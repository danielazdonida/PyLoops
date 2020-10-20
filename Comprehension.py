class Comprehension:

    def __init__(self):
        self.frase = ""

    def setFrase(self, frase):
        self.frase = frase

    def getFrase(self):
        return self.frase

    def comprehension(self):
        self.frase = [i for i in self.frase]
        return self.frase