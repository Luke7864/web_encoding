print("평문 -> ASCII 코드 16진수")
data=input(">>")

def plainTohex(a):
    a=hex(ord(a))
    return a

data=list(data)
print(data)
num=0
for i in data:
    data[num]=plainTohex(data[num])
    data[num]=data[num].replace('0x','%')
    num+=1

result=''
for i in data:
    result=result+i
print(result)