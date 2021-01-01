# import required packages
from numpy import random as np_random   # random from numpy as np_random
import random   # random


# random integer values
a = np_random.randint(3)    # random integer [0, 2], If 5 => [0,4]
b = random.randint(0,2)     # random integer [0, 2]

# random float values
c = random.random()         # random [0,1]
d = random.uniform(0,5)     # random float [0, 5]

# to check the values
print("\nRandom integer from numpy: ", a)
