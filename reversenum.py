'''write a program to find the reverse of the given number'''

num=int(input("Enter a number: "))
rev = 0
while num!=0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
print("Reverse number is:",rev)
