class student:
    def __init__(self, name, grade, gpa, major):
        self.name=name
        self.grade=grade
        self.gpa=gpa
        self.major=major

    def on_honour_roll(self):
        return self.gpa >=3.5
class Questions:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer
