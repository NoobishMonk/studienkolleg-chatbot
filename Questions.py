import recommendationSystem
import random
class Category:
    questions_dict = {}
    questions = []
    rs = recommendationSystem.RS()
    asked_questions = set()

    def __init__(self, source_path):
        Fquestions = open(f"{source_path}/QuestionsList.txt", encoding="UTF-8")
        Fanswers = open(f"{source_path}/AnswersList.txt", encoding="UTF-8")
        while True:
            qi = Fquestions.readline()
            ai = Fanswers.readline()
            if not qi:
                break
            self.questions_dict[qi] = ai
        self.questions = list(self.questions_dict.keys())
        self.rs = recommendationSystem.RS(self.questions_dict)
        self.asked_questions = set()


    def askQuestion(self):
        command = input("Du: ")
        user_question = ""
        if command == "777":
            not_asked_questions = []
            for i in range(len(self.questions)):
                if not i in self.asked_questions:
                    not_asked_questions.append(i)
            if len(not_asked_questions) == 0:
                not_asked_questions = list(range(len(self.questions)))
                self.asked_questions.clear()
            command = self.questions[random.randint(0, len(not_asked_questions))]
            print(f"Chatbot: Die Frage ist: {command}")
            user_question = command
        else:
            question_candidate = self.rs.getMatch(command)
            if question_candidate == None:
                print("Chatbot: Ich habe Sie nicht verstanden. Fragen Sie bitte noch einmal")
                return
            yesno = input(f"Chatbot: Meinen Sie diese Frage: {question_candidate} (ja/nein): ").lower()
            while not yesno in ("ja", "nein"):
                yesno = input("ja/nein: ").lower()
            if yesno == "nein":
                print("Chatbot: Ich habe Sie nicht verstanden. Fragen Sie bitte noch einmal")
                return
            user_question = question_candidate
        print(f"Chatbot: Antwort für ihre Frage: {self.questions_dict[user_question]}")
        self.asked_questions.add(self.questions.index(user_question))


categories_dict = {}
category_sources = {
    "Projekt über AVL-Bäume": "PresentationInfo",
    "Leben": "LifeInfo"
}

def askQuestion(category: str):
    if not category in categories_dict:
        categories_dict[category] = Category(category_sources[category])
    print(f"Chatbot: frag nach {category}")
    categories_dict[category].askQuestion()


def clear():
    categories_dict.clear()