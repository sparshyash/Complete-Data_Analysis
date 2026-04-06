li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),

    # Infine Loop
while (True):
    print("Hello Geek")
    break


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)