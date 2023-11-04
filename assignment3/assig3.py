#FSW Question

# class1=[
#   {"ID": 7, "Name": "Alice", "Age": 20, "Major": "Computer Science", "GPA": 3.7},
#   {"ID": 2, "Name": "Bilal", "Age": 24, "Major": "Accounting", "GPA": 3.0},
#   {"ID": 3, "Name": "Hilal", "Age": 22, "Major": "Information technology", "GPA": 2.8},
#   {"ID": 4, "Name": "Ameer", "Age": 23, "Major": "Information Technology", "GPA": 3.8}
# ]
# class2=[
#   {"ID": 1, "Name": "Eyad", "Age": 20, "Major": "Computer Science", "GPA": 3.3},
#   {"ID": 2, "Name": "Rony", "Age": 22, "Major": "Accounting", "GPA": 3.1},
#   {"ID": 3, "Name": "Hady", "Age": 22, "Major": "Accounting", "GPA": 2.6}
# ]


# def GetStudent(list,id):
#   for i in range(len(list)):
#     if list[i]["ID"]==id:
#       return list[i]
#   return "No student found."


# def GetAll(list):
#   if len(list)!=0:
#     for i in range(len(list)):
#       print(list[i], end="\n")
#   else:
#     print("List is empty")
    

# def GetStudentByMajor(list,major):
#   for i in range(len(list)):
#     if list[i]["Major"]==major:
#       print(list[i], end="\n")

      
# def AddStudent(list,id,name,age,major,gpa):
#   if len(list)!=0:
#     for i in range(len(list)):
#       if list[i]["ID"]==id:
#         return "Student already exists."
#     list.append({"ID": id, "Name": name, "Age": age, "Major": major, "GPA": gpa})
#     return "Student added successfully."
#   else:
#     list.append({"ID": id, "Name": name, "Age": age, "Major": major, "GPA": gpa})
#     return "Student added successfully."

# def FindCommonMajor(list1,list2):
#   common=[]
#   for i in range(len(list1)):
#     for j in range(len(list2)):
#       if list1[i]["Major"]==list2[j]["Major"]:
#         common.append(list1[i]["Major"])
#   return set(common)

# def DeleteStudent(list,id):
#   for i in range(len(list)):
#     if list[i]["ID"]==id:
#       del list[i]
#       return "Student deleted successfully."
#   return "Student not found."

# def AverageGPA(list):
#   sum=0
#   for i in range(len(list)):
#     sum+=list[i]["GPA"]
#   average=sum/len(list)
#   return  average




#   # I used some help in the get top students function#

# def GetTopStudents(list,n):
#   if len(list)>=n:
#     SortList=sorted(list, key=lambda student: student['GPA'], reverse=True)
#     top = SortList[:n]
#     top_student_names = tuple(student['Name'] for student in top)
#     return top_student_names
#   else:
#     return "List is too short for the given number of students"

# choice=1
# while choice!=9:
#   print("\n1.Get Student by ID \n2.Get All Students \n3.Get Students by Major \n4.Add Student \n5.Find Common Majors \n6.Delete Student \n7.Calculate Average GPA \n8.Get Top performers \n9.Exit \n- - - - - - - - - - - - - - -")
#   choice=int(input("Enter your choice: "))
#   if choice==1:
#     id=int(input("Enter ID: "))
#     print(GetStudent(class1,id))
#   elif choice==2:
#     GetAll(class1)
#   elif choice==3:
#     major=input("Enter the major: ")
#     GetStudentByMajor(class1,major)
#   elif choice==4:
#     id=int(input("Enter ID: "))
#     name=input("Enter name: ")
#     age=int(input("Enter age: "))
#     major=input("Enter major: ")
#     gpa=float(input("Enter GPA: "))
#     print(AddStudent(class1,id,name,age,major,gpa))
#   elif choice==5:
#     print(FindCommonMajor(class1,class2))
#   elif choice==6:
#     id=int(input("Enter ID: "))
#     print(DeleteStudent(class1,id))
#   elif choice==7:
#     print(AverageGPA(class1))
#   elif choice==8:
#     n=int(input("Enter number of top performers: "))
#     print(GetTopStudents(class1,n))
#   elif choice==9:
#     print("Program ends")
#     break
#   else:
#     print("Invalid choice.")



# ----------------------------------------------------------------------------------------

#FSD Question

# class1=[
#   {"Name": "Alice", "Age": 20, "Scores": (20,50,80)},
#   {"Name": "Ashraf", "Age": 23, "Scores": (50,50,50)},
# ]

# class2=[
#   {"Name": "Alice", "Age": 20, "Scores": (60,50,80)},
#   {"Name": "Eyad", "Age": 21, "Scores": (55,70,57)},
# ]

# def GetAverageScore(list):
#   if len(list)!=0:
#     for i in range(len(list)):
#         score=list[i]["Scores"]
#         avr=(score[0]+score[1]+score[2])/3
#         dic={list[i]["Name"]:avr}
#         print(dic)
#   else:
#     print("list is empty")

# def GetYoungestStudent(list):
#   if len(list)!=0:
#     min=list[0]["Age"]
#     name=list[0]["Name"]
#     for i in range(len(list)):
#       if list[i]["Age"]<min:
#         min=list[i]["Age"]
#         name=list[i]["Name"]
#     print(name)
#   else:
#     print("List is empty")

# def GetHighestScore(list):
#   if len(list)!=0:
#     name=""
#     max=0
#     for i in range(len(list)):
#       sum=list[i]["Scores"][0]+list[i]["Scores"][1]+list[i]["Scores"][2]
#       if sum>max:
#         max=sum
#         name=list[i]["Name"]
#     print(name)
#   else:
#     print("List is empty")

# def AddStudent(list,name,age,score):
#     list.append({"Name": name, "Age": age,"Scores": score})
#     return "Student added successfully."

# def RemoveStudent(list,name):
#     for i in range(len(list)):
#       if list[i]["Name"]==name:
#         del list[i]
#         return "Student deleted successfully."
#     return "Student not found."

# def GetCommonStudents(list1,list2):
#     common=[]
#     for i in range(len(list1)):
#       for j in range(len(list2)):
#         if list1[i]["Name"]==list2[j]["Name"]:
#           common.append(list1[i]["Name"])
#     return set(common)

# def FindConsistentImprovement(list):
#   l=[]
#   if len(list)!=0:
#     for i in range(len(list)):
#       if list[i]["Scores"][0]<=list[i]["Scores"][1] and list[i]["Scores"][1]<=list[i]["Scores"][2]:
#         l+=[list[i]["Name"]]
#     t=tuple(l)
#     return t
#   else:
#     return "List is empty"




# choice=1
# while choice!=9:
#   print("\n1.Get Average Score \n2.Get Youngest Student \n3.Get Highest Score \n4.Add Student \n5.Remove Student \n6.Get Common Students \n7.Find Students With Consistent Improvement \n8.Exit \n- - - - - - - - - - - - - - -")
#   choice=int(input("Enter your choice: "))
#   if choice==1:
#     GetAverageScore(class1)
#   elif choice==2:
#     GetYoungestStudent(class1)
#   elif choice==3:
#     GetHighestScore(class1)
#   elif choice==4:
#     name=input("Enter name: ")
#     age=int(input("Enter age: "))
#     score=tuple(map(int,input("Enter 3 grades : ").split(',')))
#     if score[0]>100 or score[1]>100 or score[2]>100:
#       print("Invalid grades!")
#     else:
#       print(AddStudent(class1,name,age,score))
#   elif choice==5:
#     name=input("Enter student name: ")
#     print(RemoveStudent(class1,name))
#   elif choice==6:
#     print(GetCommonStudents(class1,class2))
#   elif choice==7:
#     print(FindConsistentImprovement(class1))
#   elif choice==8:
#     print("Program ends")
#     break
#   else:
#     print("Invalid choice.")

