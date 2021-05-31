import json

book = open('book.json')
nbrPoint = 0
data = json.load(book)
chapter = ""
while True:
    number = input("Enter the chapter number between 0 and 5: ")
    if number == 0:
        chapter = "chap0"
    elif number == 1:
        chapter = "chap1"
    elif number == 2:
        chapter = "chap2"
    elif number == 3:
        chapter = "chap3"
    elif number == 4:
        chapter = "chap4"
    elif number == 5:
        chapter = "chap5"
    else:
        exit(0)
print(data[chapter]["text"])
print("question: " + data[chapter]["question"])
print("Two choices " + str(data[chapter]["choix"]["premier"]) + " or " + str(data[chapter]["choix"]["second"]))
rep = raw_input("reponse: ")
print(str(rep))
print(str(data[chapter]["reponses"]["correct"]))
if (str(rep) == str(data[chapter]["reponses"]["correct"])):
nbrPoint = nbrPoint + 1
print(nbrPoint)