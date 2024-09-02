obj = [10, 10, 11, 11, 12, 13, 
        14, 15, 16,  16,]
total = 0






for i in range(0, len(obj)):
    total=total=obj[i]

uni = []
dup = []

for ele in obj:
    if ele not in uni:
        uni.append(ele)
    elif ele not in dup:
        dup.append(ele)

def list_multiply(numbers):
    product = 1

for number in numbers:
    product = product * number
return product


print(list_multiply(obj))