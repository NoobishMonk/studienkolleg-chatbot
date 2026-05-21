import introduction, Questions, recommendationSystem
import os

os.system("cls")
introduction.introduction()
categories = ["Projekt über AVL-Bäume", "Leben"]
rs = recommendationSystem.RS(categories)
while True:
    print("""Chatbot: Wonach möchtest du fragen?
Wähle eine der Optionen: Projekt über AVL-Bäume (1), Leben (2)""")
    command = ""
    while command == "":
        command = input("Du: ")
        if command == "":
            continue
    if command.lower() == "neu":
        os.system("cls")
        introduction.introduction()
        Questions.clear()
        continue
    if command.lower() in ("halt", "stop", "end", "leave"):
        break
    if command in ('1', '2'):
        command = categories[int(command) - 1]
    else:
        command = rs.getMatch(command)
    if command in categories:
        Questions.askQuestion(command)
    else:
        print("Chatbot: Wähle nochmal")