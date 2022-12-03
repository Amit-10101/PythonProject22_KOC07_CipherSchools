
print("Name of student sperated by space")
n=input()
names=n.split()
l=len(names)
marks=[]
marksu=[]
for i in range(l):
    print("enter mark of "+names[i]+" Marks")
    me=int(input())
    marks.append(me)
ma=max(marks)
id=marks.index(ma)
#i1=n[0] i2=n[1] i3=[2]

if id==0:
    i1=1
    if marks[1]>marks[2]:
        i2=2
        i3=3
    else:
        i3=2
        i2=3
elif id==1:
    i2=2
    if marks[0]>marks[2]:
        i1=2
        i3=3
    else:
        i3=2
        i1=3
else :
    i3=1
    if marks[0]>marks[1]:
        i1=2
        i2=3
    else:
        i2=2
        i1=3


for i in range(l):
    print("enter number you want to update "+names[i]+" Marks")
    m=int(input())
    marksu.append(marks[i]+m)
toppers=[]
max=max(marksu)
g=marksu.index(max)

for i in range(l):
    if max==marksu[i]:
        toppers.append(names[i])
print("Below student have maximum marks after update")
for i in toppers:
    print(i)

def maxu(g):
    if g==0:
        i11=1
        if marksu[1]>marksu[2]:
            i22=2
            i33=3
        else:
            i33=2
            i22=3
        b=i11-i1
        c=i22-i2
        d=i33-i3

        print(f"{names[0]}'s old rank is {i1}, new rank is {i11}, rank added by {b}") 
        print(f"{names[1]}'s old rank is {i2}, new rank is {i22}, rank added by {c}") 
        print(f"{names[2]}'s old rank is {i3}, new rank is {i33}, rank added by {d}")   

    elif g==1:
        i22=1
        if marksu[0]>marksu[2]:
            i11=2
            i33=3
        else:
            i33=2
            i11=3
        b=i11-i1
        c=i22-i2
        d=i33-i3
        print(f"{names[0]}'s old rank is {i1}, new rank is {i11}, rank added by {b}") 
        print(f"{names[1]}'s old rank is {i2}, new rank is {i22}, rank added by {c}") 
        print(f"{names[2]}'s old rank is {i3}, new rank is {i33}, rank added by {d}")

    elif g==2 :
        i33=1
        if marksu[0]>marksu[1]:
            i11=2
            i22=3
        else:
            i22=2
            i11=3
        b=i11-i1
        c=i22-i2
        d=i33-i3
        print(f"{names[0]}'s old rank is {i1}, new rank is {i11}, rank added by {b}") 
        print(f"{names[1]}'s old rank is {i2}, new rank is {i22}, rank added by {c}") 
        print(f"{names[2]}'s old rank is {i3}, new rank is {i33}, rank added by {d}")
        
maxu(g)