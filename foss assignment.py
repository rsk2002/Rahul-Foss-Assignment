''' 
    Author     : Rahul S Kumar
    Roll Numer : 52
               : TRV20EC045
'''

print("Program to find the max storable amount of water")
print("Enter the heights and when finished entering input 0")

vals = []
i = 0
while True:
    i += 1
    val = int(input("Enter value "+str(i)+" = "))
    if val == 0:
        break
    vals.append(val)

# vals = [1,8,6,2,5,4,8,3,7]

print("The values are :", vals)

max_storage=0
for i in range(len(vals)):
    for j in range(i, len(vals)):
        min_h = vals[i]
        if vals[j] < min_h:
            min_h = vals[j]
        storage = min_h * abs(i-j)

        if storage > max_storage:
            max_storage = storage

print("The max storage capacity is", max_storage)