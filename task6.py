set1= (input("Enter the numbers in your set1(Seprated by space): "))
set2= (input("Enter the numbers in your set2(seprated by space): "))

x=set1.split()
y=set2.split()

set_1=set(x)
set_2=set(y)

for i in x:
    set_1[i]=set_1.get(i,0)+1
print(set_1)
for j in y:
    set_2[j]=set_2.get(j,0)+1

print(set_1)
print(set_2)