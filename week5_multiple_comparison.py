# multiple comparison
print("Enter number a:")
a=int(input())
print("Enter number b:")
b=int(input())
print("Enter number c:")
c=int(input())

average_value=(a+b+c)/3
print("Average value is:"+str(average_value))

if a>b and a>c :
    print("a is max")
    max_value=a
if b>a and b>c :
    print("b is max")
    max_value=b
if c>a and c>b :
    print("c is max")
    max_value=c
print("max value is:"+str(max_value))

if a<b and a<c :
    print("a is min")
    min_value=a
if b<a and b<c :
    print("b is min")
    min_value=b
if c<a and c<b :
    print("c is min")
    min_value=c
print("min value is:"+str(min_value))

if a>b>c or a<b<c:
    print("median is:"+str(b))
if b>a>c or b<a<c:
    print("median is:"+str(a))
if a>c>b or a<c<b:
    print("meidan is:"+str(c))

    