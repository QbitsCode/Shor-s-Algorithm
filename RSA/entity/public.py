class Public:
    def __init__(self, n, e):
        self.n = n
        self.e = e
    
    def encrypt(self, m):
        return (m**self.e) % self.n