# for i in range(0,18,):
#  print(i)
# str= "IHATEEXAMS"
# for i in str:
    # print(i)
# number=int(input("Enter number"))
# for i in range(1,11): 
#     print(number , "x",i,"=",number*i)
sumnumbers= sum(range(1,901))
print(sumnumbers)
number= int(input("Enter any number"))
flag=False
if number > 1:
    for i in range(2,number):
        if (number%i) ==0:
            flag=True
            break
if flag:
    print(number, "is divisible number")
else:
    print(number,"is prime number")
    
    
