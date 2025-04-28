word = input("Enter the Word: ")
ch = input("Enter the character: ")
i = 0
count = 0
while (i<len(word)):
    if (word[i]==ch):
        count += 1
    i += 1

print("Total number of times ", ch, "appeared in the word = ",count)