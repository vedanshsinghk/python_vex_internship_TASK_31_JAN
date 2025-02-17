text=input("Enter words with multiple frequency with spaces: ")

words= text.split()

word_count={}

for i in words:
    word_count[i]= word_count.get(i,0)+1

print(word_count)