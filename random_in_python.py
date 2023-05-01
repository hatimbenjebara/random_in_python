import numpy as np 
#generate a random integer between 1 et 10 
a = np.random.randint(1,10)
print(a)
#generate a random floating-point number between 0 and 1
a = np.random.random()
print(a)
#generate a random floating-point number between 1 and 10
a = np.random.uniform(1, 10)
print(a)
fruits = ["apple", "banana", "orange"]
a = np.random.choice(fruits)
print(a)
#shuffle the element in a list 
fruits = ["apple", "banana", "orange"]
a = np.random.shuffle(fruits)
print(a)

