list = ["Python is a thing where you can learn how to code a lot of things even for games so i like it."]
count = 0
for line in list:
    words = line.split()
    count += len(words)
    print("number of words in list:", count)