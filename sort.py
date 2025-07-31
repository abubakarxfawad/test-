array=[]

for i in range(1,5):
    num=int(input(f"enter {i} number: "))
    array.append(num)

array.sort()
print(f"sorted array: {array}")