import context
from context import *


class Game:
    def __init__(self, given_Ques) -> None:
        self.given_Ques = given_Ques

    def start_Game(self):
        current_Question = list(self.given_Ques)[0]
        return current_Question

    def restart_Game(self):
        a = input().lower()
        if a != "yes":
            self.end_Game()
        else:
            return self.start_Game()

    def end_Game(self):
        sys.exit()

    def answerYes(self, current_Question):
        current_Question = self.given_Ques[current_Question][0]

        return current_Question

    def answerNo(self, current_Question):
        current_Question = self.given_Ques[current_Question][1]

        return current_Question


Ques = Ques(Game(Ques_dict), Game(Ques_dict))

while True:
    Ques.show_Ques()




