import random

def List(names):
    randomised = ''.join(random.sample(names, len(names)))
    print(randomised)


names = input()
List(names)