#Day 3 Part 2
with open("binary_output.txt","r") as sig:
    list1=sig.read().split()


length=len(list1)
data=list1
dataCO2=list1

while len(data) > 1:
    for i in range(len(data[0])):
        summe=0
        ones=[]
        zeros=[]
        
        for num in data:
            number=int(num[i])
            summe+=int(number)

            if number==0:
                zeros.append(num)
            else:
                ones.append(num)
            
        if summe >= len(data)/2:
            data = [i for i in ones]
        else:
            data = [i for i in zeros]
            
print("oxygen = ",int(data[0],2))

while len(dataCO2) > 1:

    for i in range(len(dataCO2[0])):
        summe=0
        ones=[]
        zeros=[]
        z=0
        o=0
        
        for num in dataCO2:
            number=int(num[i])
            summe+=int(number)

            if number==0:
                z=z+1
                zeros.append(num)
            else:
                o=o+1
                ones.append(num)
        
        if z>0 and o>0:
            if summe >= len(dataCO2)/2:
                dataCO2 = [i for i in zeros]
            else:
                dataCO2 = [i for i in ones]
print("CO2 = ",int(dataCO2[0], 2))
O2=int(data[0], 2)
CO2=int(dataCO2[0], 2)
