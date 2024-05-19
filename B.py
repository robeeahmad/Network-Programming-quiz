num = eval(input('Please Enter Your Number to calc the factorial: '))
f = 1
try:
    if num <0:
        print("Your number is negative!")
    if num == 0 or num == 1:
        print(f)
    while num > 0:
        f *= num
        num -= 1
finally:
        print(f)    
           
    