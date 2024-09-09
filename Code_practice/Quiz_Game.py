# This is a simple Quiz Game

class Question:
    def __init__(self, question_text, choices, correct_answer):
        self.question_text = question_text
        self.choices = choices
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

    def __str__(self):
        return f"{self.question_text}\n" + "\n".join(f"{i+1}. {choice}" for i, choice in enumerate(self.choices))


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for question in self.questions:
            print(question)
            user_answer = int(input("Your answer (1-4): ")) - 1
            if question.check_answer(question.choices[user_answer]):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.correct_answer}\n")
        self.get_score()

    def get_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")


def main():
    quiz = Quiz()

    q1 = Question(
        "What is the capital of France?",
        ["Berlin", "Madrid", "Paris", "Rome"],
        "Paris"
    )
    q2 = Question(
        "What is the largest planet in our solar system?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        "Jupiter"
    )
    q3 = Question(
        "Which programming language is known as the 'language of the web'?",
        ["Python", "JavaScript", "Java", "C++"],
        "JavaScript"
    )

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)

    quiz.start()

if __name__ == "__main__":
    main()
