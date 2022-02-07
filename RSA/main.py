#apt install gcc
#apt install libgmp3-dev
#pip install miller-rabin
from RSA import CreateKeys, GenerateKeysFromPublic


keys = CreateKeys.execute(1, 30)
print("N: ", keys.n)
print("E: ", keys.e)
print("D: ", keys.d)

m = 12
print("Original Message: ", m)
c = keys.encrypt(m)
print("Encrypted Message: ", c)
d = keys.decrypt(c)
print("Decrypted Message: ", d)

print("\n From public:")
gkeys = GenerateKeysFromPublic.execute(13, 11, 7, 143)
print("N: ", gkeys.n)
print("E: ", gkeys.e)
print("D: ", gkeys.d)

m = 14
print("Original Message: ", m)
c = gkeys.encrypt(m)
print("Encrypted Message: ", c)
d = gkeys.decrypt(c)
print("Decrypted Message: ", d)