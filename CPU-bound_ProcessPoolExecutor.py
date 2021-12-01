from hashlib import md5
from random import choice
import concurrent.futures

def is_prime():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
with concurrent.futures.ProcessPoolExecutor(max_workers = 1000) as executor:
    executor.map(is_prime())