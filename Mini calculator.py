num1= int(input("Enter your first number"))
num2= int(input("Enter your second number"))
print("Choose an operation +,-,*,/")
operation= (input("Enter ypur operation"))
if operation == "+":
  result= num1 + num2
elif operation ==  "-":
  result= num1 - num2
elif  operation == "*":
  result=  num1 * num2
elif  operation == "/":
  if num2 != 0:
    result= num1/num2
  
  else:
    result== "Cannot divide by 0!"
else:
  result= "Invalid Operation !"
print("Result",result)
