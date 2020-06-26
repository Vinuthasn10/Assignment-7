
#Length of the string
str=input("Enter the string:")
c=len(str)
print("Length of the string is",c) 


#Frequency of Charcters
str=input("Enter the string:")
ch=input("Enter the character to be checked:")
count=0
for letter in str:
    if letter==ch:
        count=count+1
print("The",ch,"Letter","in",str,"has repeated for",count,"times")


#Swapping the characters of string
def strs(a, b):
    n_a=b[:2] + a[2:]
    n_b=a[:2] + b[2:]
    return n_a+' '+n_b
x=input("Enter the first string:")
y=input("Enter the second string:")
print("The Original String:",x+y)
print("The Swapped String:",strs(x,y))


#Upper and Lower cases
str=input("Enter any string:")
print("The String in Upper case is:",str.upper())
print("The String in Lower case is:",str.lower())



#New line removal
str="I'm Iron Man\n"
print(str)
print(str.rstrip())


#Substring occurrences in a Main String 
str=input("Enter the string:")
ch=input("Enter the substring presence to be checked:")
print(str.count(ch))


#Conversion of string into list
import ast
str="['Im the one, the world call me by name IRON MAN']"
print(ast.literal_eval(str))


#Deletion of character from a string
def char_dlt(str, n):
    x= str[:n]
    y=str[n+1:]
    return x+y
ch=input("Enter the string:")
n=int(input("Enter the index where the character is to be deleted:"))
print(char_dlt(ch,n))


str=input("Enter the string:")
for index,char in enumerate(str):
    print(char)
 
 
#Length of string without len function
str=input("Enter the string:")
count=0
for i in str:
      count=count+1
print("Length of the string is:")
print(count)
