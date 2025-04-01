
print("WELCOME TO IZIFIN TECHNOLOGY!")
work_experience = int(input("Enter your years of experience: "))
age = int(input("Input your age: "))

if work_experience > 25 and age >= 55:
      atr = 5_600_000
      print("Work-Experience: ",work_experience)
      print("Age: ", age)
      print("Annual Tax Revenue: ", atr)
elif work_experience > 20 and age>= 45:
       atr =  4_480_000
       print("Work-Experience: ",work_experience)
       print("Age: ", age)
       print("Annual Tax Revenue: ", atr)
        
elif work_experience > 10 and age>= 35:
      atr = 1_500_000
      print("Work-Experience: ",work_experience)
      print("Age: ", age)
      print("Annual Tax Revenue: ", atr)
elif work_experience < 10 and age < 35:
      atr =  550_000
      print("Work-Experience: ",work_experience)
      print("Age: ", age)
      print("Annual Tax Revenue: ",atr)
else:
      print("Invalid input!")                    
