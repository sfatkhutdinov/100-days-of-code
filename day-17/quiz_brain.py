class QuizBrain:
    """This class handles all the logic that runs the quiz
    """

    def __init__(self, question_list):
        """Initializer for the QuizBrain class

        Args:
            question_list ([string]): The list of questions that is passed to
            the class during creation.
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Checks if the question list have any more questions left

        Returns:
            Bool: returns True if there questions available. 
            At the end of the quiz it will print the completion message
            and prints the final score.
        """
        if self.question_number == len(self.question_list):
            print("You've completed the quiz!")
            print(f"Your final score was: {self.score}/{self.question_number}")
        return self.question_number < len(self.question_list)

    def next_question(self):
        """This method presents the current question and accepts the user's answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True or False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """This method checks the user answer for correcteness by comparing the 
        it to the answers available in the data file

        Args:
            user_answer (str): User input
            correct_answer (str): The correct answer from the data file
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')
