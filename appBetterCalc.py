from  appFunction import sum,sub,mul,div

num1 = float(input("enter number1:"))
op = input("enter operator:")
num2 = float(input("enter number2:"))

result=0
if(op=="+"):
    result=sum(num1,num2)
elif(op=="-"):
    result=sub(num1,num2)
elif(op=="*"):
    result=mul(num1,num2)
elif(op=="/"):
    result=div(num1,num2)
else:
    print("Invalid Operator")

print("result is:",result)