#Assignment 1

#question 1

n=int(input(""))
fact=1
if n>0:
  for i in range(1,n+1):
   fact*=i
  print (fact)

########################################################
#question 2

n=int(input(""))
list=[]
for i in range(1,n+1):
  if n%i==0:
    list+=[i]
print(list)

########################################################
#question 3

def reverseString(s):
  rev=""
  for char in s:
    rev=char+rev
  return rev

#######################################################
#question 4 

def even_numbers(list):
  even= []
  for number in list:
      if number % 2 == 0:
         even.append(number)
  return even

########################################################
#question 5

def strong_password(password):
  if len(password)>=8:
    up=low=n=s=False
    for i in range (len(password)):
      if password[i].isdigit():
          n=True
      elif password[i].isupper():
          up=True
      elif password[i].islower():
          low=True
      elif password[i]=='#'or password[i]=='$'or      password[i]=='!'or  password[i]=='?':
          s=True
    if up==True and low==True and n==True and s==True:
      print("Strong Password")
    else:
      print("Weak Password")
  else:
    print("password should be at least 8 characters long")


strong_password("1234A567!a")

#question 6

def valid_IP(ip):
  valid=False
  oct=ip.split(".")
  if len(oct)==4:
    for i in range (len(oct)):
      if oct[i].isdigit():
        val=int(oct[i])  
        if oct[i][0]==0 and len(oct[i])!=1:
          valid=False
          break
        elif val>=0 and val<=255:
          valid=True
        else:
          valid=False
          break
      else:
        valid=False
        break
  else:
    valid=False
  if valid==True:
    return "valid ip address"
  else:
    return "invalid ip address"
  
########################################################

#question 7

def calculations(list):
  sum=0
  for i in range(len(list)):
    sum=list[i]
    
  avg=sum/len(list)

  mode=0
  for j in range(len(list)):
    jcount=0
    for k in range(len(list)):
        if list[j]==list[k]:
            jcount+=1
        if jcount>=mode:
            mode=jcount
            return mode
    
  
  max=0
  min=list[0]
  for m in range(len(list)):
    if list[m]>max:
        max=list[m]
    elif list[m]<min:
        min=list[m]
  return max,min
  
  
  print("average:",avg)
  print("mode:",mode)
  print("max:",max)
  print("min:",min)
    
    



  




    