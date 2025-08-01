number=[]

for i in range(10):
    num=int(input(f"enter number {i+1}: "))
    number.append(num)

n=len(number)

for i in range(n):
    for j in range(0, n-i-1):
        if number [j] > number [j+1]:

            number[j],number[j+1]  = number[j+1],number[j]

print("sorted numbers:",number)