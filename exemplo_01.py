import random
import time

def numero_aleatorio():
    return random.randint(1,10)

if __name__ == "__main__":
    while True:
        num = numero_aleatorio()
        print(num)
        time.sleep(1)
