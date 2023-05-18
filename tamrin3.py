
Phrase = input("Phrase=")
Phrase = Phrase.replace(" ", "")
new_Phrase =""
for item in Phrase:
    if  item in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        new_Phrase+="."
    elif item.islower():
       new_Phrase+=item.upper()   
    else:
        new_Phrase+=item.lower()
print(new_Phrase)

