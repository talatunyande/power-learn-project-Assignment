my_list = []
#adding 10,20,30,and 40 to the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"my_list :{my_list}")
my_list.insert(1,15)

print(f"my_list :{my_list}")
#extending to add 50,60,70
my_list.extend([50,60,70])
print(f"my_list :{my_list}")
#removing the last element
my_list.pop()
print(f"my_list :{my_list}")
#Sorting the list in ascending order
my_list.sort()
print(f"my_list :{my_list}")

#finding the index of 30 in my_list
my_list.index(30)
print(my_list.index(30))