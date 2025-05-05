def check_bit():
    print("Welcome to the Bit Checker Game")
    print("Enter a number,I will print if it is a 0 or a 1\n")
    while True:
        bit=input("Enter a number(0,1)and type 'exit' if you want to exit: ")
        if bit.lower() =="exit":
            print("Thanks For playing!Bye")
            break
        if bit=='0':
            print("It's a Zero bit\n")
        if bit=='1':
            print("It's a Ones bit\n")
        else:
            print("Oops,That's Not a valid Bit.Enter only 0's or 1s\n")
check_bit()