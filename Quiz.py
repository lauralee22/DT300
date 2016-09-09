#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gouldenl
#
# Created:     09/09/2016
# Copyright:   (c) gouldenl 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

"""Code Listing 1.14"""


import random

class Question:
    """ Authors: Gray, Harper, Garner, Robins; Date: 2 December 2012
        Purpose: This class supports the class Quiz.  Instances of this class represent individual
        questions in the quiz, and possible answers, with the correct answer at a random place in
        the list of possible answers (dummies).
    """

    def __init__(self, question, answer, dummies):
        """ Constructor for instances of Question, sets up the instance variables representing
            the question, and calls self.set_answer to set up the instance variable representing
            the possible answers (including the correct answer).
        """
        self.question = question
        self.answer = answer
        self.dummies = dummies
        self.set_answers()

    def set_answers(self):
        """ Inserts correct answer at random place in the list of possible answers (dummies). """
        self.answers = self.dummies
        self.answers.insert(random.randrange(len(self.dummies) + 1), self.answer)
class Quiz:
    """ Authors: Gray, Harper, Garner, Robins; Date: 2 December 2012
    Purpose: This class manages a (text only) multi-choice quiz.  It will be extended in future versions with a
    graphical user interface, and access to files of multiple questions and answers.  This class is supported by the
     class Question.  Instances of Question represent the individual questions (and answers of the quiz).  In this
     version of the program there are only two questions.  """

    def __init__(self):
        """ Creates a list containing two Question objects by passing the Question constructor
            - a string representing the question
            - a string representing the correct answer
            - a list of strings representing the dummy answers
        """
        self.questions = [Question("What is the capital of Mongolia?",
                 "Ulan Bator",
                 ["Vladivostok", "Astana","Lhasa"]),
                 Question("Who wrote 'The Picture of Dorian Gray?",
                 "Oscar Wilde",
                 ["George Bernard Shaw", "Evelyn Waugh", "Somerset Maugham"]),
                 Question("Who wrote 'Fifty Shades of Grey?",
                 "E. L. James",
                 ["G. R. R. Martin", "J. K. Rowling", "S. L. Meyer"]),
                 Question("What is the name of the fourth Harry Potter book?",
                 "Harry Potter and the Goblet of Fire",
                 ["Harry Potter and the Chamber of Secrets", "Harry Potter and the Philosphers Stone", "Harry Potter and the Sorcerers Stone"])]

    def take_quiz(self):
        """ This method is the main driver for the quiz. It loops through questions,
            presents each one and its possible answers. It then calls the process_answer method
            passing in a reference to the current question.
        """
        for q in self.questions:    # for each question object in the list of questions
            print( q.question )           # print the question
            for i in range(len(q.answers)):     # print the possible answers
                print("\t" + str(i ) + "\t" + q.answers[i])
            print()
            self.process_answer(q)  # get answer from user and give appropriate response

    def process_answer(self, q):
        """ This method reads in the user's answer (should be an int in the range 0 to the number
            of possible answers).  It gives an appropriate response to the user's answer.
            The while loop continues until the user inputs an int that is in range. Once they do
            their answer is checked against the correct one to see if it matches.
            Remember input comes in as a string and must be converted to int.
        """
        user_answer = -1
        # keeps looping until user's input is an int in range
        while not 0 <= user_answer < len(q.answers):
            a = input("Please type the number of your answer here: ")
            try:
                user_answer = int(a)  # if input is not an int we go to the except clause
                if not 0 <= user_answer < len(q.answers):
                    # input is not in range no further action is taken (the while loop will repeat)
                    print("\nThat was out of range\n")
                elif user_answer == q.answers.index(q.answer):
                    # input is equal to the index of the correct answer (the while loop will end)
                    print("\nWell Done!!\n")
                else:
                    # input not equal to the index of the correct answer (the while loop will end)
                    print("\nIncorrect, the answer is " + q.answer + "\n")
            except ValueError:
                # if user's input is not an int this executes (anticipating errors is good design!)
                print("\nThat was not a sensible input. Integers only please.\n")
#main routine
if __name__ == "__main__":
    text_quiz = Quiz()
    text_quiz.take_quiz()