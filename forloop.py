#sum of first natural numbers
n=int(input("Enter a number:"))
sum=0

#i=1,n+1
for i in range(1,n+1):
    sum=sum+i
    print (sum)

#reverse a string
s1=input("Enter your string:")

s2= ('')
for i in s1:
    s2=i+s2

print("\nThe Original String=",s1)
print("The Reversed String=",s2)

#reverse order
n1= int(input("Enter number:"))
print("Numbers from {0} to {1}".format(n1,1))

for i in range(n1,0,-1):
    print(i)