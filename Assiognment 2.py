#access a particular element in set

set ={"Abhi","Ronaq","Akash","Vipul"}
print("Abhi" in set)
print("Vimal" in set)

#Difference between discard() and remove()
#the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

set2 = {"java","python","c","c++"}

#remove() method

set2.remove("python")
print(set2)

#dicard()method 

set2.discard("pythons")
print(set2)

#intersection_update()
#The intersection-update() method returns a set that contains the similarity between two or more sets.


x = {"apple", "banana", "cherry"}
y = {"google", "banana" ,"microsoft", "apple"}
x.intersection_update(y)
print(x)


#symmetric_difference_update()
#The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items

x1= {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
x1.symmetric_difference_update(y1)
print(x1)

#symmetric_difference()

element1={"apple","orange","banana","pineapple","guava"}
element2={"bus","car","train","orange","guava"}
#BY USING symmetric_differnce()
#this method will return a new set that contains only the items that are not present in both the sets
element3 = element1.symmetric_difference(element2)
print(element3)

#dict()
mydict={
    "student":"Abhiraj",
    "id":3262,
    "company":"cloudeq"
}
#BY USING copy() this does not take any parameter
dict1=mydict.copy()
print(dict1)

#BY USING dict() it takes dictionary as a parameter
dict2=dict(mydict)
print(dict2)

#append()by converting tuples into a list

tup1=("apple","banana","orange","guava")
#append by converting to list
x4=list(tup1)
x4.append("lichi")
tup1=tuple(x4)
print(tup1)

#add tuple to tuple
tup2=("pineapple",)
tup1+=tup
print(tup1)