number1 = int(input("please enter first number :"))
number2 = int(input("please enter second number :"))
Operation = input("please enter the operational sign :")
Operational_output = number1 and Operation and number2
if Operation == "+":
    print (number1 +number2)
elif Operation == "-" :
    print (number1 - number2)
elif Operation == "*":
    print (number1 * number2)
elif Operation == "/":
    print (number1 /number2)
elif Operation == "%" :
    print (number1 % number2)
else :
    print ("Invalid input")


