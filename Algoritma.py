user_height = float(input("Enter your height in meters: "))
user_weight = float(input("Enter your weight in kilograms: "))

user_indeks = user_weight / user_height ** 2

if user_indeks < 18.5:
    print("Weak")
elif user_indeks < 25:
    print("Normal")
elif user_indeks < 30:
    print("Overweight")
else:
    print("Obese")
#-------------------------------------------------------------------
print("\n\n")
#-------------------------------------------------------------------
vize1 = float(input("Enter your first vize note: "))
vize2 = float(input("Enter your second vize note: "))
final = float(input("Enter your final note: "))

note=(vize1*30/100)+(vize2*30/100)+(final*40/100)

if(note>=90):
     print("AA")
elif(note>=85):
     print("BA")
elif(note>=80):
     print("BB")
elif(note>=75):
     print("CB")
elif(note>=70):
     print("CC")
elif(note>=65):
     print("DC")
elif(note>=60):
     print("DD")
elif(note>=55):
     print("FD")
else:
     print("FF")
