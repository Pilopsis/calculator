print("enter operation")
print("1:add\n2:subtruct\n3:multiply\n4:divide\n")
operator=input()

if operator== "1":
    num1=int(input("enter 1st number"))
    num2=int(input("enter 2nd number"))
    print("Answer"+str(int(num1)+int(num2)))
elif operator== "2":
    num1=int(input("enter 1st number"))
    num2=int(input("enter 2nd number"))
    print("Answer"+str(int(num1)-int(num2)))
elif operator== "3":
    num1=int(input("enter 1st number"))
    num2=int(input("enter 2nd number"))
    print("Answer"+str(int(num1)*int(num2)))
elif operator== "4":
    num1=int(input("enter 1st number"))
    num2=int(input("enter 2nd number"))
    print("Answer"+str(int(num1)/int(num2)))
else:
    print("invalid operand!!")

