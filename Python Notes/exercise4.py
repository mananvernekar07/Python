print("Odd Numbers from 1 to 20")
for i in range(1,21,2):
        print(i)
        i += 1
print("")

print("Table of 57")
for i in range(57,571,57):
        print(i)  
print("")  

print("Multiples of 3 from 1 to 50 except 15")
for i in range(1,51):
    if i==15:
       continue
    if i%3 == 0:
        print(i)
print("")

print("Get a divisible number")
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
for i in range(1,1001):
    if i%a == 0 and i%b ==0:
        print(i,"is divisible by both",a,"and",b)
        break

         