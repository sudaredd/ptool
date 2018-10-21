friends=["Sherif","Bill","David","James"]

print(friends)
print(friends[1])
print(friends[2:])
print(friends[0:4])
friends[1]="Abdo";
print(friends[1])

lucky_numbers = [1,4,6,2,90];

#friends.extend(lucky_numbers);
friends.append("Prem")
print(friends)
print(friends.pop())
print(friends)
print(friends.index("David"))
friends.sort();
print(friends)
friends.reverse();
print(friends)
friends1 = friends.copy();
friends.clear();
print("friends",friends)
print("friends1",friends1)