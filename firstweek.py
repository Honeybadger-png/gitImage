# week3 python practice

def getNumber():
    n= 2
    a=[]
    for i in range(0,n):
        elem=int(input("enter your exam result: "))
        a.append(elem)
    avg=sum(a)/n
    
    while  avg<50:
        makeUp=int(input("what is the result of your makeup exam: "))
        a.append(makeUp)
        n= n+1
        avg=sum(a)/n
        if n==3:
            break
    if avg>=50 and avg<60:    
        print("average is : ",round(avg,2))
        print("You passed ! with D")
    elif avg>=60 and avg<70:
        print("average is : ",round(avg,2))
        print("You passed ! with C")
    elif avg>=70 and avg<80:
        print("average is : ",round(avg,2))
        print("You passed ! with B")
    elif avg>=80 and avg<90:
        print("average is : ",round(avg,2))
        print("You passed ! with A")
    elif avg>90 and avg<=100:
        print("average is : ",round(avg,2))
        print("You passed ! with AA")
    

getNumber()
