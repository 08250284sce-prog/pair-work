#asking input from users 
Name = str(input("Enter Your Name:"))
M1 = float(input("Enter Marks of Module1:"))
M2 = float(input("Enter Marks of Module2:"))
M3 = float(input("Enter Marks of Module3:"))
M4 = float(input("Enter Marks of Module4:"))
Attendance = float(input("Enter your Attendance:"))
#output for name and attendance
print("Student Name:",Name)
print("Attendance:%.2f " % Attendance,"%")
#Calculating avg
A = (M1+M2+M3+M4)/4
print("Average:",A)
#cheking pass or fail
if A>=50 and Attendance>=90:
    print("Status:Pass showala!!")
else:
    print("Status:Fail sho wala!")
#cheking grade
if A>=90 and Attendance>=90:
    print("Grade:A[Excellent]")
elif A>=80 and Attendance>=90:
    print("Grade:B[V.Good]")
elif A>=70 and Attendance>=90:
    print("Grade:C[Good]")
elif A>=50 and Attendance>=90:
    print("Grade:D[Okay]")
else:
    print("Grade:F[Paycha lam cho!!!]")
#cheking elegibility
if A>=90 or A>=80 or A>50 and Attendance>=90:
    print("Eligable for Reward")
else:
    print("No Reward!SORRY!")
