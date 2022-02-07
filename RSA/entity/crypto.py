class Crypto:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

    def encrypt(self, m):
        return (m**self.e) % self.n

    def decrypt(self, c):
        return (c**self.d) % self.n

