def SI(P, R, T):
 return P * (1+(R/100)*T)
def CI(P,R,n,t):
 return P * (1+(R/n))^(n*t)
def AP(PMT,R,n,t):
 return PMT*((1+(R/n))^(n*t) -1)/(R/n)

print("Welcome to my Calculator!")
print("Choose a calculation:")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. Annuity Plan")
user_input =int(input("Enter user_input (1/2/3):"))

if user_input == 1:
 P= float(input("Enter Principal Amount: "))
 R= float(input("Enter annual interest rate(%): "))
 T = float(input("Enter time(years): "))
 print("Final Amount:", SI(P,R,T))

elif user_input == 2:
   P= float(input("Enter the Principal Amount: "))
   R= float(input ("Please enter the annual interest rate: "))
   n= int(input("Please enter number of times interest applied per year: "))
   t= float(input("Please enter time(years): "))
   print("Final Amount:", CI(P,R,n,t))

elif user_input == 3:
 PMT= float(input("Enter the periodic payment amount: "))
 R= float(input ("Please enter the annual interest rate: "))
 n= int(input("Please enter number of times interest applied per year: "))
 t= float(input("Please enter time(years): "))
 print("Final Amount:", AP(PMT,R,n,t))          

else:
 print("Invalid input! Please input 1,2 or 3")
 