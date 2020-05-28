import json
from difflib import get_close_matches
data = json.load(open("dictionaryData.json"))
def translate(word):
    word = word.lower()
    if word in data:
       return data[word]
    elif word.title() in data:
       return data[word.title()]
    elif word.upper() in data:
       return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("If Yes press y, if Not press n ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("I'm afraid! think like I don't know the word")
        else:
            return("Wrong input, Please check the word")
    else:
        print("I'm afraid! think like I don't know the word")

word = input("Search a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
