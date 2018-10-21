from appClass import  Questions
question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
     "What color are straberries?\n(a) Blue\n(b)Red",
]

questions=[
    Questions(question_prompts[0],"a"),
    Questions(question_prompts[1],"b"),
    Questions(question_prompts[2],"b")
]

def run_quiz(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if(answer==question.answer):
            score += 1
    print("you got ",str(score), " out of",str(len(questions)))

run_quiz(questions)
