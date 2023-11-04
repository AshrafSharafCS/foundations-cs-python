def CountDigit(num):
  if num<9:
    return 1
  else:
    return 1 + CountDigit(num//10)


def findMax(list):
  if len(list)==0:
      return 0
  max = findMax(list[1:])
  if list[0] > max:
      return list[0]
  else:
      return max

x=1
while x>0 and x<5:
  print ("\n-  -  -  -  -  -  -  -  \n1. Count Digits \n2. Find Max \n3. Count Tag \n4. Count Normalized Columns \n5. Exit \n-  -  -  -  -  -  -  -  -  -  \n")
  print("Enter an option:")
  x=int(input())
  if x==1:
    print("Enter a number")
    number=int(input())
    print(CountDigit(number))
  elif x==2:
    l = list(map(int, input("Enter a list of integers separated by spaces: \n").split()))
    print(findMax(l))
  else:
    print("The End!!")
    break
