import random
import json

class QuizHandler:
    def __init__(self, quiz_file):
        with open(quiz_file, 'r') as f:
            self.quizzes = json.load(f)

    def get_quiz(self, topic):
        """Fetch a quiz for a specific topic."""
        return random.choice(self.quizzes.get(topic, []))
