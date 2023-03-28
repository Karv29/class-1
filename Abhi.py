
#type Casting 
#integer to float

a = 23
print (type(a))
print(float(a))

#float to integer 
b = 4.90
print(type(b))
print(int (b))

#int to string 
c = 3
print(type(c))
print(str(c))

#string to int 
d = "abhi"
print(type(d))

#list in python

list1 = [1, 2, "Python", "Program", 15.9]      
list2 = ["Amy", "Ryan", "Henry", "Emma"]   
  
# printing the list  
print(list1)  
print(list2)  
print(list1[4])
print(list2[2])

#tuple in python

tuple = (33,'python','bmw',4.0)
print(tuple)
print(tuple[3])
print(tuple[-2])

#dictonary in python
Employee = {"Name": "Abhi", "Age": 23, "salary":25000,"Company":"Cloud Eq"}      
print(Employee)
print(Employee["Age"])
print(Employee["Company"])
print(Employee["Name"])
print(Employee["salary"])

#Sets in python

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}    
print(Days)    
Days.add("Saturday")
Days.add("Sunday")
print(Days)