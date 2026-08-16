#Check even or odd
def eveodd(number):
    if number%2 == 0:
       print(number,"is an even number")
    else:
       print(number,"is an odd number")

eveodd(4)
eveodd(7)

#Count number of vowels in a string
def vowel(sentence):
   count = 0
   for char in sentence.lower():
      if char in "aeiou":
         count +=1
   print(count,"vowels in",sentence) 

vowel("Computer Engineering")

#To find number is prime or not
def prime(number):
   if number <= 1:
      print(number,"is not a prime number")
      return

   for i in range(2,number):
      if number%i == 0:
           print(number,"is not a prime number")
           return

   print(number,"is a prime mumber")

prime(13)
prime(70)

#To calculate average of marks
def avg(marks):
    if len(marks) == 0:
       print("List is empty")
       return 0
    
    result = sum(marks)/len(marks)
    print(f"{result} is the average marks")
    return result
    
student_marks = [12,14,17,18,9,8]
avg(student_marks)