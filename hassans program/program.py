numbers=[]

while True:
    num=input("enter a number or x to stop: ")
    if num.lower()=="x":
        break
    else:
        numbers.append(int(num))
# after loops
if numbers:
    print(f"you entered:{numbers}")
    print("maximum entered",max(numbers))
    print("minimum entered",min(numbers))
else:
    print("no number entered")