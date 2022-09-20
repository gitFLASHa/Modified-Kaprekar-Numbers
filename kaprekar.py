#given a range. try except is used as int() can receve null inputs when the digit size is 1 as there wont be a second digit to add

def kaprekarNumbers(p, q):
  kn = []  
  for number in range(p, q+1):
    x = str(number**2)
    lenx = len(x) #index+1
    if(x==str(number)):
      kn.append(x)
      continue
    tillindex = lenx//2
 
    try:
      partsum = int(x[0:tillindex])+int(x[tillindex:len(x)+1])
    except:
      partsum = int(x[tillindex:len(x)+1])  
    if(partsum == number):
      kn.append(number)
   
  if len(kn) > 0:
    for each in kn:
      print(each, end=" ")
  else:
    print("INVALID RANGE")
