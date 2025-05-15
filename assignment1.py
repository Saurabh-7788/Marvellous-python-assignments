#def fun():
   # print("hello from fun")
#fun()

def chcknum(no):
    if no % 2 == 0:
        print("THIS IS AN EVEN NO")
    else:
        print("THIS IS AN ODD NO")

def addition(no1,no2):
    result=no1+no2
    return result

print("enter first no")
no1=int(input())

print("enter second no")
no2=int(input())

ans=addition(no1,no2)

print("addition is",ans)

for i in range(5):
    print("Marvellous")

for a in range(10,1,-1):
    print(a)

