def translate(phrase):
    tranlation = "";
    for letter in phrase:
        if letter in "aeiouAEIOU":
            tranlation = tranlation + "g"
        else:
            tranlation = tranlation + letter
    return  tranlation;
print(translate(input("Enter a phrase:")))
