rollNumberWiseDataStore=dict()
mobileNumberWiseDataStore=dict()
student=[]
def addStudent():
  try:
     roll_number=int(input("Enter roll number:"))
     if roll_number<=0: raise ValueError
  except:
     print("Invalid roll number")
     return
  if roll_number in rollNumberWiseDataStore:
      print(f"{roll_number} has been alloted to {rollNumberWiseDataStore[roll_number][1]}")
      return
  name=input("Enter name: ")
  moblieNumber=input("Enter your mobile number:")
  if mobileNumber in mobileNumberWiseDataStore:
     print(f"{mobileNumber} exist against roll number {mobileNumberWiseDataStore[mobileNumber][0]}")
     return 
  while True:
    save=input("Save (Y/N):")
    if save not in "ynYY":
         print("Press Y/N")
         continue
    else:break
  if save in "yY":
      student=(roll_number,name,mobileNumber)
      rollNumberWiseDataStore[roll_number]=student
  def displayListOfStudents():
    if len(students)==0:
       print("No students added")
       return 
    sno=0
    pageSize=3
    newPage=True
    line="-"*68
    for student in students:
        if newPage:
           print(line)
           print("S.No.".center(10," "),"Roll no.".ljust(30," "),"Name.".ljust(15," "),"Mobile.".ljust(15," "))
           print(line)
           newPage=False
        sno+=1
        (roll_number,name,mobile_number)=student
        print(str(sno).rjust(10," "),str(roll_number).rjust(10," "),name.rjust(30," "),mobile_number.ljust(15," "))
        if sno%pageSize==0 or sno==len(students):
           print(line)
           input("Press enter to continue....")
           newPage=True

while True:
  print("1.Add")
  print("2.Edit")
  print("3.Delete")
  print("4.Search")
  print("5.List")
  print("6.Exit")
  try:
     choice=int(input("Enter the number from 1 to 6:"))
     if choice<1 or choice>6: raise ValueError
  except:
     print("Invalid choice")
     continue
  if choice==1: addStudent()
  if choice==2: edit_Student()
  if choice==3: deleteStudent()
  if choice==4: searchStudent()
  if choice==5: displayListOfStudents()
  if choice==6: break
print("Bye take care and have a good time")
  