import time
import pipes
import os

dir = './print_outs/'

while True:
    files = os.listdir(dir)
    for file in files:
        f = open(dir + file)
        print(f.read(), end='', flush=True)
        os.remove(dir + file)