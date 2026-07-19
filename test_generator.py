from src.generator import generate_quiz

quiz = generate_quiz(
    "Cricket",
    "Medium"
)

print(type(quiz))
print()

for q in quiz:
    print(q["question"])
    print(q["options"])
    print("Answer:", q["answer"])
    print()