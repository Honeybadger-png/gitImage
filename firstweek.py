# if statement


number = 5
if number <= 5:
    print("number is less than 5") 

def getNumber():
    n= int(input("how many number will be added"))
    a=[]
    for i in range(0,n):
        elem=int(input("enter a number: "))
        a.append(elem)
    avg=sum(a)/n
    print("average is :",round(avg,2))

getNumber()
