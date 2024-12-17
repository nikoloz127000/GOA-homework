def count_items(arr,item):
    count = 0
    for i in arr:
        if i == item:
            count += 1
    return count

print(count_items(['hello','this','is','this'], 'this'))