operation = input("Please Choose you operation (add) (sub) (multi) (div): ")

if operation == "add" :
    num1 = input("First: ")
    num2 = input("Second: ")
    sum = int(num1)+int(num2)
    print("Answer: " + str(sum))
elif operation == "sub" :
    num3 = input("First: ")
    num4 = input("Second: ")
    sum = int(num3) - int(num4)
    print("Answer: " + str(sum))
elif operation == "multi" :
    num5 = input("First: ")
    num6 = input("Second: ")
    sum = int(num5) * int(num6)
    print("Answer: " + str(sum))
elif operation == "div" :
    num7 = input("First: ")
    num8 = input("Second: ")
    sum = int(num7) / int(num8)
    print("Answer: " + str(sum))
else :
    print("Please type a operation.")
