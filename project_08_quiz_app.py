# Simple Quiz Application

questions = [
    {"q": "What is the extension of Python files?", "a": ".py"},
    {"q": "Which keyword is used to define a function in Python?", "a": "def"},
    {"q": "Which function is used to take input from the user?", "a": "input"}
]

score = 0
print("--- Simple Python Quiz ---")

for item in questions:
    ans = input(item["q"] + " : ")
    if ans.strip().lower() == item["a"].lower():
        print("Correct!\n")
        score = score + 1
    else:
        print(f"Wrong! Correct answer: {item['a']}\n")

print(f"Quiz Completed! Your Score: {score}/{len(questions)}")
