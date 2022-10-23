#WAP to find given number is Even or Odd.
i=3
while(i>0):
    num=int(input('Enter the number to check no. is Even/Odd: '))
    if(num%2==0):
        print("Entered no. is Even.")
    else:
        print('Entered no. is Odd.')
    i-=1

