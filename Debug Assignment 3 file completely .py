#---------------------Assigment no 3 part 1------------------#
s1 = float(input("Enter your Math subjct marks: 100 out of .... "))

s2 = float(input("Enter your English subjct marks: 100 out of .... "))

s3 = float(input("Enter your Urdu subjct marks: 100 out of .... "))

s4 = float(input("Enter your physics subjct marks: 100 out of .... "))

s5 = float(input("Enter your computer subjct marks: 100 out of .... "))

total_marks = (s1+s2+s3+s4+s5)

percentage = (total_marks/500) * 100

print("you get marks 500 out of ", total_marks)

print("your percentage is ", percentage)

if percentage <= 95:
    grade = "A++"

elif percentage <= 90:
    grade = "A+"
    
elif percentage <= 85:
    grade = "A"
    
elif percentage <= 80:
    grade = "B++"
    
elif percentage <= 75:
    grade = "B+"
    
elif percentage <= 70:
    grade = "B"
    
elif percentage <= 65:
    grade = "C++"
    
elif percentage <= 60:
    grade = "C+"
    
elif percentage <= 55:
    grade = "C"

elif percentage <= 50:
    grade = "D"

else:
    grade = "F" 

print("And your Grade is ", grade)
    
#------------------ Assigement no 3 part 2 -----------------#
x = int(input("enter your year to check leap year  "))

if (x % 400 == 0) or (x % 4 == 0 and x % 400 != 0):
    print("this is leaf year")
else:
    print("its not leap year")

#---------------- Assigement no 3 part 3 ---------------#

C = float(input("Enter temperature in celsius to converts between fahrenheit and kelvin"))

K = C + 273.15
F = (K - 273.15 ) * (5/9)+32

print("convert to kelvin", K)
print("convert to fahrenheit", F)

f = float(input("Enter temperature in fahrenheit to converts between celsius and kelvin"))

c = (f - (32)) * (5/9) 
K=(f-32) * (9/5)+273.15


print("convert to celsius", K)
print("convert to kelvin", F)

x = float(input("Enter temperature in kelvin to converts between celsius and fahrenheit"))

y= x-273.15
z = 26.85 * (9/5 )+32


print("convert to celsius", y)
print("convert to fahrenheit", z)



#---------------- Assigement no 3 part 4 ---------------#

us1 = int(input("enter first side of triangle "))
us2 = int(input("enter secound side of triangle "))
us3 = int(input("enter third side of triangle "))

if (us1==us2==us3):
    print("This is Equiritral triangle")

elif (us1==us2)or (us1==us3) or(us2==us3) or (us2==us1):
    print("This is isoscalene triangle")
    
elif (us1!=us2!=us3):
    print("This is Equiritral triangle")
else:("some thing was wrong")




