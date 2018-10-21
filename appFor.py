friends=["Balakonda","Kuladeep","Sreenivas"]

print("------------with foreach-------------------")
for friend in friends:
    print(friend)

print("-------------------with range-------------------")
for index in range(len(friends)):
    print(friends[index])
print("-------------------raise_to_power-------------------")

def raise_to_power(base_num, power_num):
    result = 1;
    for index in range(power_num):
        result = result * base_num;

    print("result is",result)

raise_to_power(2,4)

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0,10],
]

for row in number_grid:
    for column in row:
        print("value of number grid",column)