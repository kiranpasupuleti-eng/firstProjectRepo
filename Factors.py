n=int(input("Enter a number:"))
i=1
s=0
while i!=n:
  if n%i==0:
    print(i)
    s+=i
  i+=1
print("Sum Of Factors is:",s)
if s==n:
  print("Perfect Number")
else:
  print("Not A Perfect Number")
