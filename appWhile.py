num=1

while num <=10:
    print(num)
    num+=1

print("done while loop")

secret_word="bhavya"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while secret_word != guess and not (out_of_guesses):
    if guess_limit > guess_count:
        guess=input("Enter secret word: ")
        guess_count+=1
    else:
        out_of_guesses=True

if not (out_of_guesses):
    print("you won!")
else:
    print("you lose sucker!")