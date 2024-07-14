'''
python program to check whether given num is armstrong
'''
x = input("Enter a number: ")
sum=0
p = len(x)
for i in x:
    sum+=int(i) ** p
if sum == int(x):
    print(f"{x} is an armstrong")
else:
    print(f"{x} is not an armstrong")
