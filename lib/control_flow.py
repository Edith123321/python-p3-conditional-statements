#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


   

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 75:
        return  "It's perfect out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:  # Multiple of both 3 and 5
        return "FizzBuzz"
    elif num % 3 == 0:  # Multiple of 3 only
        return "Fizz"
    elif num % 5 == 0:  # Multiple of 5 only
        return "Buzz"
    else:
        return num  # Return the integer directly




def calculator(operation, num1, num2):
   if operation == "+" :
      return num1+num2
   elif operation == "-":
       return num1-num2
   elif operation =="/":
       return num1/num2
   elif operation == "*":
       return num1*num2
   else:
       print( "Invalid operation!")
       return None
       
       

   
