class Private:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def decrypt(self, c):
        return (c**self.d) % self.n