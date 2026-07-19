from src.generator import generate_quiz

quiz = generate_quiz(
    "Cricket",
    "Medium"
)

print(type(quiz))
print(type(quiz[0]))
print()

for question in quiz:
    print(question.question)
    print(question.options)
    print("Answer:", question.answer)
    print("Explanation:", question.explanation)
    print()