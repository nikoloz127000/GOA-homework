l = []
n = int(input("Enter Lenght of list:"))
for i in range(1,n+1):
    e = int(input("Enter Element:"))
    l.append(e)
print(l)
even = []
odd = []
for j in l:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
        print("Odd Element list:", odd)
        print("Even Element list:", even)