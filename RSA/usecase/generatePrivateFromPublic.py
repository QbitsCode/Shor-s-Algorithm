from RSA.entity.private import Private
from RSA.entity.public import Public
from RSA.usecase.createKeys import xgcd, getD
from RSA.entity.crypto import Crypto

class GeneratePrivateFromPublic:
    def __init__(self) -> None:
        pass

    def execute(p, q, public: Public):
        t = (p-1)*(q-1)
        d = getD(public.e, t)

        return Private(public.n, d)