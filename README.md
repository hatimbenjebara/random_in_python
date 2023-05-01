# random_in_python
In python, we can provide random is a built-in library that generate a random numbers of different type such as integers, floating-point numbers.
The random module contain a various function, such as, the random() function to create a random numbers. Example1, 
import numpy as np 
#generate a random integer between 1 and 10
a = random.randint(1,10)
print(a)
#generate a random floating-point number between 0 and 1
a = random.random()
print(a)
#generate a random floating-point number between 1 and 10
a = random.uniform(1, 10)
print(a)
#pick a random element from a list 
fruits = [“apple”, “banana”, “orange”]
a = np.random.choice(fruits)
print(a)
#shuffle the element in a list 
fruits = [“apple”, “banana”, “orange”]
a=np.random.shuffle(fruits)
print(a) 
