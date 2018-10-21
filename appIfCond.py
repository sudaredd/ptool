is_male=False
is_tall=True

if is_male and is_tall:
    print("you are male and tall")
elif is_male and not (is_tall):
    print("you are male but not tall")
elif not (is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are neither male nor tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return  num1
    elif num2 >= num1 and num2 >= num3:
        return num2;
    else:
        return num3;

print("maximum num is ",max_num(3,40,5))

def str_compare(str1, str2):
    if(str1==str2):
        print("both strings are eqal")
    else:
        print("String are non equals")

str_compare("Sudar","Darsan")
str_compare("hello","hello")
