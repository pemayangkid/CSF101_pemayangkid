fruits = ["apple", "banana", "cherry"]

fruits.append("date")
fruits.extend(["elderberry", "fig"])

fruits.insert(1, "blackberry")

fruits.remove("cherry")
last_fruit = fruits.pop()

print(fruits[0]) 
print(fruits[-1])  

print(fruits[1:4])  

fruits.sort()
print(fruits) 

squares = [x**2 for x in range(5)]
print(squares)