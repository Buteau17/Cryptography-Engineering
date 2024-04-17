import random

with open("InsecureRandom.bin", "wb") as file:
    file.write(bytes(random.getrandbits(8) for _ in range(1048576)))