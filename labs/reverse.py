#to find reverse of a number

num = int(input("number is: "))
rev = 0

#while num!=0:
#    rem = num%10
#    rev = (rev*10)+rem
#    num= num//10
#print("Reverse number is: ", rev)

number = str(num)
print (number)

li = []
for i in number:
    li.append(i)
li.reverse()
print(li)

srt= ""

for i in range(0,len(number)):
    srt += str(li[i])

print("srt is ", srt)
print("reverse of number is: ", int(srt))
