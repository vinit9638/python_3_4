# Make a stack and only allow push and pop function in it.

stack = []


print("Enter push for insertion")
print("Enter pop for deletion ")
while True:
    ch = input("Enter your ope...")
    if ch == "1":
        num = int(input("Enter the number you want to push :- "))
        stack.append(num)
    elif len(stack)!=0 and ch == "pop":
        num = int(input("Enter the number you want to pop :- "))
        stack.pop()
    elif ch == 3:
        break
print("your updated stack is :- ",stack)
