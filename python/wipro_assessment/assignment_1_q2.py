sentence = input("enter sentence: ")
count = 0

for ind, chr in enumerate(sentence):
    if chr == 'a':
        count += 1
print("count of 'a': ", count)