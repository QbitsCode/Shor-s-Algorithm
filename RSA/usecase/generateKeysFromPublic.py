from RSA.usecase.createKeys import xgcd, getD
from RSA.entity.crypto import Crypto

class GenerateKeysFromPublic:
    def __init__(self) -> None:
        pass

    def execute(p, q, e, n):
        t = (p-1)*(q-1)
        d = getD(e, t)

        return Crypto(n, e, d)