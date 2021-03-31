def return_10():
    return 10

def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(str):
    return len(str)

def join_string(str1, str2):
    return str1 + str2  

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)

# def number_to_full_month_name(num1):
#     months = ["January", "February", "March", "April", "May", 
#     "June", "July", "August", "September", "October", "November", "December"]
#     if num1 == 

def number_to_full_month_name(num1):
    months = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 
    6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    return months[num1]

def number_to_short_month_name(num1):
    months = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 
    6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    return months[num1][0:3]

def volume_of_cube(num):
    return num * num * num

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(num1):
    return (num1 - 32) * 5/9
