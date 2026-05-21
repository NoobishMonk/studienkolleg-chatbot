import difflib

class RS:
    questions = []

    def __init__(self, questions=None):
        self.questions = questions


    def getMatch(self, user_question: str):
        prefix = ""
        cnt_prefixes = 0
        for q in self.questions:
            if len(q) >= len(user_question) and q[:len(user_question)] == user_question:
                prefix = q
                cnt_prefixes += 1
        if cnt_prefixes == 1:
            return prefix
        match = difflib.get_close_matches(user_question, self.questions, n=1)
        return match[0] if match else None